#!/usr/bin/env python3
"""
小红书发布包守门 — PreToolUse hook。

拦截写入 xhs.md / XHS 图卡文案时的两类风险：
1. 反引流禁词（命中即 deny，封号级风险）
2. 字数超标（标题 >20 / 正文 >1000，超标即 deny；接近上限给 warning）

输入：Claude Code hook 经 stdin 传入的 JSON（tool_name + tool_input）。
退出码：
  0 = 放行（可能带 stderr warning）
  2 = 阻断（stderr 说明原因，Claude 会看到并改）

仅对路径含 `xhs.md` 的写入生效，其它一律放行。
规则来源：CLAUDE.md「小红书反引流硬规则」+「硬性字数限制」。
"""
import json
import re
import sys

# —— 反引流禁词（命中即阻断）。来源：CLAUDE.md 禁词表 ——
# 注意：右下角水印「雷码工坊笔记」是品牌签名、合规例外，但 xhs.md 是 caption
# 文案文件，正文里不该出现该词，故此处仍纳入扫描（写文案 ≠ 图片水印）。
BANNED = [
    "公众号", "微信公众号", "关注公众号", "扫码关注", "扫码",
    "加微信", "加 v", "加v", "私信加", "微信号", "vx", "VX",
    "雷码工坊笔记", "雷码工坊",
    "B站", "B 站", "bilibili", "哔哩哔哩",
    "抖音同名", "同名抖音",
    "telegram", "Telegram", "TG群", "电报",
    "二维码",
]
# 外站完整 URL（小红书剥外链 + 引流风险）
URL_RE = re.compile(r"https?://[^\s)]+", re.I)
# 允许的站内/通用域名白名单（理论上 xhs.md 不该有任何 URL，留空=全拦）
URL_WHITELIST = ()

TITLE_MAX = 20
BODY_MAX = 1000
BODY_WARN = 900


def visible_len(s: str) -> int:
    """可见字符数：去掉首尾空白后按字符计（含标点/emoji/空格/换行内的字符）。"""
    return len(s)


def get_payload():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # 拿不到输入就放行，不阻塞正常流程
    tool = data.get("tool_name", "")
    ti = data.get("tool_input", {}) or {}
    path = ti.get("file_path", "") or ti.get("path", "")
    # 汇总所有将写入的文本
    chunks = []
    if "content" in ti:
        chunks.append(ti["content"])
    if "new_string" in ti:
        chunks.append(ti["new_string"])
    for e in ti.get("edits", []) or []:
        if isinstance(e, dict) and "new_string" in e:
            chunks.append(e["new_string"])
    return path, "\n".join(c for c in chunks if isinstance(c, str))


def check_title(text, problems):
    """启发式：扫 markdown 里疑似标题行（'标题'字样后的内容、# 行）。"""
    for line in text.splitlines():
        raw = line.strip()
        m = re.match(r"^#{1,3}\s*(.+)$", raw)
        if m:
            cand = m.group(1).strip()
        elif re.search(r"标题", raw) and ("：" in raw or ":" in raw):
            cand = re.split(r"[:：]", raw, 1)[-1].strip().strip("`*」「\"' ")
        else:
            continue
        # 去掉行内标注的字数说明，如「（18 字）」
        cand = re.sub(r"[（(]\s*\d+\s*字[)）]", "", cand).strip()
        if cand and visible_len(cand) > TITLE_MAX:
            problems.append(
                f"标题超 {TITLE_MAX} 字（{visible_len(cand)} 字）：{cand}"
            )


def main():
    path, text = get_payload()
    if "xhs.md" not in path.lower():
        sys.exit(0)
    if not text.strip():
        sys.exit(0)

    problems = []   # 阻断级
    warnings = []   # 提示级

    # 1) 禁词
    lower = text.lower()
    for w in BANNED:
        if w.lower() in lower:
            problems.append(f"出现反引流禁词「{w}」")

    # 2) 外站 URL
    for u in URL_RE.findall(text):
        if not any(d in u for d in URL_WHITELIST):
            problems.append(f"出现外站 URL：{u}")

    # 3) 标题字数
    check_title(text, problems)

    # 4) 正文字数（整体启发式：取最长的非标签段落估算）
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    longest = max((visible_len(p) for p in paras), default=0)
    if longest > BODY_MAX:
        problems.append(f"疑似正文段落超 {BODY_MAX} 字（{longest} 字）")
    elif longest > BODY_WARN:
        warnings.append(f"正文接近上限（{longest} 字 / {BODY_MAX}），留点缓冲")

    if warnings and not problems:
        sys.stderr.write("⚠️ XHS 提醒：\n  - " + "\n  - ".join(warnings) + "\n")

    if problems:
        sys.stderr.write(
            "🚫 XHS 守门拦截（封号/截断风险，先改再写）：\n  - "
            + "\n  - ".join(problems)
            + "\n替代 CTA：收藏 / 点赞 / 评论区聊 / 评论区扣 1 / 关注我 / 下篇见\n"
        )
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
