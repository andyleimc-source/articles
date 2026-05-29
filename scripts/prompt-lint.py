#!/usr/bin/env python3
"""
配图 prompt 品牌色 Linter — PostToolUse hook（非阻断，只提示）。

写入 prompts/*.md（出图 prompt）后扫一遍，提示：
- 禁用色（暖橙/珊瑚/紫色渐变/纯黑 #000）
- 缺水印（应含「雷码工坊笔记」字样的渲染要求）
- 缺字形约束（带文字的图应写明 Chinese glyphs must render correctly…）

规则来源：CLAUDE.md「配图配色」「配图必须带水印」「配图文字规则」。
退出码恒为 0（PostToolUse 不阻断写入，仅 stderr 提醒）。
"""
import json
import re
import sys

# 禁用色：v1 已废弃的暖橙/珊瑚 + 紫色渐变 + 纯黑
BANNED_COLORS = [
    "#E89B4B", "#e89b4b", "#E8A87C", "#e8a87c",
    "#000000", "#000 ", "#000;", "#000\"", "#000'",
]
BANNED_WORDS = [
    "orange", "coral", "purple gradient", "violet",
    "neon", "cyberpunk", "霓虹", "暖橙", "珊瑚",
]
WATERMARK_HINT = ["雷码工坊", "watermark", "水印"]
GLYPH_HINT = ["glyph", "garbled", "字形", "no garbled", "render correctly"]
# 判断这张图是否含文字（含则应有字形约束）
HAS_TEXT_HINT = ["title", "subtitle", "标题", "副标题", "文字", "label", "标签", "caption"]


def get_payload():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    ti = data.get("tool_input", {}) or {}
    path = ti.get("file_path", "") or ti.get("path", "")
    chunks = []
    if "content" in ti:
        chunks.append(ti["content"])
    if "new_string" in ti:
        chunks.append(ti["new_string"])
    for e in ti.get("edits", []) or []:
        if isinstance(e, dict) and "new_string" in e:
            chunks.append(e["new_string"])
    return path, "\n".join(c for c in chunks if isinstance(c, str))


def main():
    path, text = get_payload()
    if not re.search(r"prompts/.*\.md$", path, re.I):
        sys.exit(0)
    if not text.strip():
        sys.exit(0)

    lower = text.lower()
    notes = []

    hits = [c for c in BANNED_COLORS if c in text]
    hits += [w for w in BANNED_WORDS if w.lower() in lower]
    if hits:
        notes.append("禁用色/风格词：" + ", ".join(sorted(set(hits)))
                     + " → 换品牌色（米白 #FAF7F0 / 墨黑 #0E1116 / 磷绿 #1AB87C / 石墨 #3A4151 / 雾蓝 #9CB4CC / 砖灰 #6E6259）")

    if not any(h.lower() in lower for h in WATERMARK_HINT):
        notes.append("未见水印要求 → 加「雷码工坊笔记」右下角小水印（≤6% 宽、~60% 透明、石墨/砖灰）")

    if any(h.lower() in lower for h in HAS_TEXT_HINT) and not any(h.lower() in lower for h in GLYPH_HINT):
        notes.append("图含文字但缺字形约束 → 加 'Chinese glyphs must render correctly, no garbled characters, kerning correct'")

    if notes:
        sys.stderr.write("🎨 配图 prompt 提醒（非阻断）：\n  - " + "\n  - ".join(notes) + "\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
