#!/usr/bin/env python3
"""cc-radar evaluate: 从候选 id 拉出元信息 → 建文章脚手架 → 调 claude -p 跑测评。

用法：
    python3 scripts/evaluate.py 2026-04-28-01
    python3 scripts/evaluate.py 2026-04-28-01 --dry-run   # 只建脚手架不调 claude
    python3 scripts/evaluate.py 2026-04-28-01 --step claude  # 只重跑 claude（已有脚手架）
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # cc-radar/
ARTICLES_ROOT = ROOT.parent  # /Users/andy/Desktop/articles/
CAND_DIR = ROOT / "data" / "candidates"
PROMPT_PATH = ROOT / "prompts" / "evaluate.md"


def find_candidate(cand_id: str) -> dict:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-\d+$", cand_id)
    if not m:
        raise SystemExit(f"候选 id 格式错: {cand_id}（应为 YYYY-MM-DD-NN）")
    date_str = m.group(1)
    jpath = CAND_DIR / f"{date_str}.json"
    if not jpath.exists():
        raise SystemExit(f"找不到候选文件: {jpath}")
    data = json.loads(jpath.read_text(encoding="utf-8"))
    for c in data.get("candidates", []):
        if c["id"] == cand_id:
            return c
    raise SystemExit(f"在 {jpath} 里找不到候选 {cand_id}")


def slugify(feature_name: str, cand_id: str) -> str:
    s = feature_name.lower()
    s = re.sub(r"[^a-z0-9-]+", "-", s).strip("-")
    if not s or s == "unknown":
        s = f"feature-{cand_id}"
    return f"cc-{s}"


def write_scaffold(slug: str, cand: dict) -> Path:
    dest = ARTICLES_ROOT / slug
    if dest.exists():
        print(f"[evaluate] {dest} 已存在，跳过脚手架")
        return dest
    (dest / "demo").mkdir(parents=True)

    source_md = f"""# SOURCE — {cand['cc_feature_name']}

- **候选 id**：{cand['id']}
- **来源**：@{cand['author']} · {cand['source_url']}
- **DeepSeek 评分**：{cand['score']}
- **关键词命中**：{', '.join(cand.get('keywords', []))}

## 摘要
{cand['summary']}

## 为什么值得测
{cand['why_worth_testing']}

## 建议 demo
{cand['suggested_demo']}

## 原推内容
```
{cand['raw_text']}
```
"""
    (dest / "SOURCE.md").write_text(source_md, encoding="utf-8")

    article_md = f"""<img src="cover.png">

# {cand['cc_feature_name']}：{cand['summary'].rstrip('。')}

> 测评草稿 by cc-radar · 候选 {cand['id']} · 来源 {cand['source_url']}

## 钩子

<!-- 一句话讲为什么这个功能值得知道。从一个具体场景或者「我以为是 X，结果是 Y」切入。 -->

## 这是什么

<!-- 简洁地说清这个功能是什么。引用官方文档或原推。 -->

## 怎么用（实测）

<!-- 这是核心。贴 demo/ 里的日志关键片段（10-30 行）。 -->

## 我在哪卡住了

<!-- 真实记录。如果哪步跑不通、行为出乎意料、文档过期 —— 写出来。 -->

## 给读者的建议

<!-- 落地建议：什么场景适合用，什么场景不要用。 -->

## 一句话总结

<!-- 收束。 -->
"""
    (dest / "article.md").write_text(article_md, encoding="utf-8")
    print(f"[evaluate] 脚手架已建: {dest}")
    return dest


def run_claude(dest: Path, slug: str, cand: dict) -> int:
    prompt_template = PROMPT_PATH.read_text(encoding="utf-8")
    user_msg = (
        f"请按下面的任务说明，给候选 {cand['id']}（{cand['cc_feature_name']}）写测评。\n"
        f"你当前 cwd 是 {dest}。\n"
        f"先读 {dest}/SOURCE.md 和 {ARTICLES_ROOT}/WRITING.md，然后跑实测、写草稿。\n\n"
        f"---\n\n{prompt_template}"
    )

    cmd = [
        "claude",
        "-p",
        "--add-dir",
        str(ARTICLES_ROOT),
        "--allow-dangerously-skip-permissions",
        user_msg,
    ]
    print(f"[evaluate] 调起 claude -p，cwd={dest}")
    print(f"[evaluate]   prompt 长度 {len(user_msg)} chars")
    try:
        proc = subprocess.run(cmd, cwd=dest, check=False)
        return proc.returncode
    except FileNotFoundError:
        print("[error] 找不到 claude CLI", file=sys.stderr)
        return 127


def maybe_cover(dest: Path, cand: dict) -> None:
    # 配图：先占位，让用户后续手动调 baoyu-cover-image
    # 自动调 skill 在 headless 流里复杂——先 TODO，落 cover-prompt.md
    prompt_md = f"""# Cover prompt — {cand['cc_feature_name']}

把下面交给 baoyu-cover-image：

```
Notion 插画风文章封面，主题是 Claude Code 的 "{cand['cc_feature_name']}" 功能。
背景米白 #FAF7F0，主体墨黑 #0E1116，强调色磷绿 #1AB87C。
{cand['summary']}
flat illustration、柔和 pastel 配色、手绘感不规整描边、大量留白、editorial 风格。
右下角小水印「雷码工坊笔记」，石墨色 #3A4151 透明度 60%。
Chinese glyphs must render correctly, no garbled characters.
```

跑：`Skill baoyu-cover-image` 然后把生成的图重命名为 `cover.png` 放到本目录。
"""
    (dest / "cover-prompt.md").write_text(prompt_md, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cand_id", help="候选 id，如 2026-04-28-01")
    ap.add_argument("--dry-run", action="store_true", help="只建脚手架，不跑 claude")
    ap.add_argument("--step", choices=["scaffold", "claude", "cover"], help="只跑某一步")
    args = ap.parse_args()

    cand = find_candidate(args.cand_id)
    slug = slugify(cand["cc_feature_name"], args.cand_id)
    print(f"[evaluate] 候选 {cand['id']} → {slug}")

    step = args.step
    if step in (None, "scaffold"):
        dest = write_scaffold(slug, cand)
    else:
        dest = ARTICLES_ROOT / slug
        if not dest.exists():
            raise SystemExit(f"{dest} 不存在，先跑 --step scaffold")

    if step in (None, "cover"):
        maybe_cover(dest, cand)

    if args.dry_run:
        print("[evaluate] --dry-run，跳过 claude")
        return 0

    if step in (None, "claude"):
        rc = run_claude(dest, slug, cand)
        if rc != 0:
            print(f"[evaluate] claude 退出码 {rc}", file=sys.stderr)
            return rc

    print(f"[evaluate] 完成 → {dest}")
    print(f"[evaluate] 下一步：")
    print(f"  1. cd {dest} && 检查 article.md / demo/")
    print(f"  2. 按 cover-prompt.md 出封面")
    print(f"  3. Skill humanizer-zh 跑去 AI 味")
    print(f"  4. commit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
