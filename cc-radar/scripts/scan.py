#!/usr/bin/env python3
"""cc-radar scan: 读 xradar raw → 白名单 + 关键词过滤 → 去重 → DeepSeek 打分 → 出候选。

用法：
    python3 scripts/scan.py                 # 跑今天
    python3 scripts/scan.py --date 2026-05-17  # 跑指定日期（dry-run / 回放）
    python3 scripts/scan.py --no-llm        # 跳过 LLM 打分，只出原始命中列表（调试）
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib import request, error

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.yaml"
DATA_DIR = ROOT / "data"
CAND_DIR = DATA_DIR / "candidates"
HISTORY_PATH = DATA_DIR / "history.json"
PROMPT_PATH = ROOT / "prompts" / "select.md"


def load_yaml(path: Path) -> dict:
    """简易 YAML 解析（避免依赖 PyYAML）。只支持 cc-radar/config.yaml 用到的子集：
    顶层 key: value 标量 + key: 后跟缩进列表（- item）。
    """
    out: dict = {}
    cur_key = None
    cur_list: list | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if cur_list is None:
                raise ValueError(f"列表项无对应 key: {line}")
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            cur_list.append(val)
            continue
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            # 剥掉行内注释（但不剥引号内的 #）
            if v and not v.startswith('"'):
                hash_idx = v.find("#")
                if hash_idx >= 0:
                    v = v[:hash_idx].rstrip()
            if v == "":
                cur_list = []
                out[k] = cur_list
                cur_key = k
            else:
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1]
                # 数字
                try:
                    if "." not in v:
                        v_cast: int | float | str = int(v)
                    else:
                        v_cast = float(v)
                except ValueError:
                    v_cast = v
                out[k] = v_cast
                cur_list = None
                cur_key = k
    return out


def load_env_file(env_path: Path) -> None:
    """读 xradar 的 .env，把 DEEPSEEK_* 灌进 os.environ。"""
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def today_str() -> str:
    # 东八区今天（xradar 也是按东八跑的）
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")


def load_history() -> set[str]:
    if not HISTORY_PATH.exists():
        return set()
    return set(json.loads(HISTORY_PATH.read_text(encoding="utf-8")))


def save_history(seen: set[str]) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    HISTORY_PATH.write_text(
        json.dumps(sorted(seen), ensure_ascii=False, indent=2), encoding="utf-8"
    )


def collect_tweets(raw_dir: Path, date_str: str, accounts: list[str]) -> list[dict]:
    """从 xradar/data/raw/<date>/<account>.json 收集推文。"""
    day_dir = raw_dir / date_str
    if not day_dir.exists():
        return []
    items: list[dict] = []
    for acc in accounts:
        p = day_dir / f"{acc}.json"
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[warn] 读 {p} 失败: {e}", file=sys.stderr)
            continue
        for t in data.get("tweets", []):
            if t.get("isReply"):
                continue
            items.append(
                {
                    "id": str(t.get("id") or ""),
                    "url": t.get("url") or "",
                    "text": t.get("text") or "",
                    "author": (t.get("author") or {}).get("userName") or acc,
                    "createdAt": t.get("createdAt") or "",
                    "likeCount": t.get("likeCount") or 0,
                    "viewCount": t.get("viewCount") or 0,
                }
            )
    return items


def keyword_hit(text: str, keywords: list[str]) -> list[str]:
    low = text.lower()
    hits = []
    for kw in keywords:
        if kw.lower() in low:
            hits.append(kw)
    return hits


def call_deepseek(system_prompt: str, user_payload: str, model: str) -> tuple[str, dict]:
    """复用 xradar/scripts/digest.py 的 call_deepseek 模式。"""
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY 未设置（检查 xradar/.env）")
    base = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1").rstrip("/")
    body = json.dumps(
        {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_payload},
            ],
            "temperature": 0.3,
            "stream": False,
        }
    ).encode("utf-8")
    req = request.Request(
        f"{base}/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        raise RuntimeError(f"DeepSeek HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:400]}")
    return data["choices"][0]["message"]["content"], data.get("usage") or {}


def extract_json_array(s: str) -> list:
    """从 LLM 输出里抠 JSON 数组——容忍 ```json ``` 包裹和首尾闲谈。"""
    s = s.strip()
    if "```" in s:
        # 取首个 ``` 块
        parts = s.split("```")
        for p in parts:
            p = p.strip()
            if p.startswith("json"):
                p = p[4:].strip()
            if p.startswith("["):
                s = p
                break
    # 抠到最外层 [...]
    start = s.find("[")
    end = s.rfind("]")
    if start == -1 or end == -1:
        raise ValueError(f"找不到 JSON 数组:\n{s[:500]}")
    return json.loads(s[start : end + 1])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today_str(), help="YYYY-MM-DD，默认今天（东八区）")
    ap.add_argument("--no-llm", action="store_true", help="跳过 DeepSeek，只出关键词命中列表")
    ap.add_argument("--ignore-history", action="store_true", help="不用 history.json 去重（回放用）")
    ap.add_argument("--raw-dir", help="覆盖 config 里的 xradar_raw_dir（测试用）")
    args = ap.parse_args()

    cfg = load_yaml(CONFIG_PATH)
    load_env_file(Path(cfg.get("xradar_env_file", "")))

    raw_dir = Path(args.raw_dir or cfg["xradar_raw_dir"])
    accounts = cfg.get("accounts", [])
    keywords = cfg.get("keywords", [])
    threshold = int(cfg.get("score_threshold", 70))
    max_n = int(cfg.get("max_candidates_per_day", 5))
    model = cfg.get("deepseek_model", "deepseek-v4-flash")

    date_str = args.date
    CAND_DIR.mkdir(parents=True, exist_ok=True)

    tweets = collect_tweets(raw_dir, date_str, accounts)
    print(f"[scan] {date_str}: 白名单内拉到 {len(tweets)} 条推文")
    if not tweets:
        out_json = CAND_DIR / f"{date_str}.json"
        out_json.write_text(
            json.dumps({"date": date_str, "candidates": [], "note": "原始数据为空"}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return 0

    # 关键词命中
    hits = []
    for t in tweets:
        kw = keyword_hit(t["text"], keywords)
        if kw:
            t["keywords"] = kw
            hits.append(t)
    print(f"[scan] 关键词命中 {len(hits)} 条")

    # 去重
    history = set() if args.ignore_history else load_history()
    new_hits = [t for t in hits if t["id"] not in history]
    print(f"[scan] 去重后剩 {len(new_hits)} 条")

    if not new_hits:
        out_json = CAND_DIR / f"{date_str}.json"
        out_json.write_text(
            json.dumps({"date": date_str, "candidates": [], "note": "无新命中"}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return 0

    # LLM 打分
    candidates: list[dict] = []
    if args.no_llm:
        for i, t in enumerate(new_hits):
            candidates.append(
                {
                    "id": f"{date_str}-{i+1:02d}",
                    "tweet_id": t["id"],
                    "score": 0,
                    "cc_feature_name": "unknown",
                    "summary": t["text"][:80],
                    "why_worth_testing": "(--no-llm 跳过打分)",
                    "suggested_demo": "",
                    "source_url": t["url"],
                    "author": t["author"],
                    "raw_text": t["text"],
                    "keywords": t.get("keywords", []),
                }
            )
    else:
        system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
        payload = json.dumps(
            [
                {"id": t["id"], "author": t["author"], "text": t["text"], "url": t["url"]}
                for t in new_hits
            ],
            ensure_ascii=False,
            indent=2,
        )
        print(f"[scan] 调 DeepSeek 打分（{len(new_hits)} 条）...")
        raw, usage = call_deepseek(system_prompt, payload, model)
        try:
            scored = extract_json_array(raw)
        except Exception as e:
            print(f"[error] LLM 输出解析失败: {e}", file=sys.stderr)
            print(raw, file=sys.stderr)
            return 1
        score_map = {str(it.get("id")): it for it in scored}
        for t in new_hits:
            it = score_map.get(t["id"])
            if not it:
                continue
            candidates.append(
                {
                    "tweet_id": t["id"],
                    "score": int(it.get("score") or 0),
                    "cc_feature_name": it.get("cc_feature_name") or "unknown",
                    "summary": it.get("summary") or "",
                    "why_worth_testing": it.get("why_worth_testing") or "",
                    "suggested_demo": it.get("suggested_demo") or "",
                    "source_url": t["url"],
                    "author": t["author"],
                    "raw_text": t["text"],
                    "keywords": t.get("keywords", []),
                }
            )
        print(f"[scan] DeepSeek usage: {usage}")

    # 排序 + 阈值 + Top N
    candidates.sort(key=lambda x: x["score"], reverse=True)
    survivors = [c for c in candidates if c["score"] >= threshold][:max_n]
    # 给每个生还者派 id（日期-序号）
    for i, c in enumerate(survivors):
        c["id"] = f"{date_str}-{i+1:02d}"

    out_json = CAND_DIR / f"{date_str}.json"
    out_json.write_text(
        json.dumps(
            {
                "date": date_str,
                "threshold": threshold,
                "total_hits": len(hits),
                "after_dedup": len(new_hits),
                "candidates": survivors,
                "all_scored": candidates,  # 留全量便于调参
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[scan] 写入 {out_json}（{len(survivors)} 个候选过阈值）")

    # 落 history（只记 LLM 真跑过的；--no-llm 不落，避免污染）
    if not args.no_llm and not args.ignore_history:
        for c in candidates:
            history.add(c["tweet_id"])
        save_history(history)

    return 0


if __name__ == "__main__":
    sys.exit(main())
