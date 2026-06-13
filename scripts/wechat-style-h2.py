#!/usr/bin/env python3
"""
把 baoyu 生成的 article.html 里的 H2 大标题，从默认「磷绿填充块」改写成
雷码工坊「荧光笔 A 档」样式：标题墨黑无底色，文字下半段压一层半透明磷绿色带。

为什么不用 baoyu 主题改：CLI 不支持注入自定义 H2 CSS，4 个内置主题的 H2
要么是绿块（simple/default）要么不合品牌。直接后处理生成的 html 最干净可控。

样式规则（严格遵守 BRAND.md）：
- H2 文字：墨黑 #0E1116，左对齐，不要 display:table / 不要 background 填充块
- 荧光带：linear-gradient(transparent 58%, rgba(26,184,124,.28) 0)
  —— 只压文字下半段（58% 以下），半透明，文字仍清晰
- 荧光带必须包在文字外层 inline <span>，贴着字；加在 h2 块上会变成整行通栏底色（错）

用法：
    ./scripts/wechat-style-h2.py <article-dir>/article.html
    原地改写，原文件备份为 article.html.bak-<时间戳>

幂等：已处理过的 H2（含荧光 span 标记）会跳过，可重复运行。
"""
import re
import sys
from datetime import datetime
from pathlib import Path

# ---- 荧光笔 A 档参数（定稿，要调改这里）----
GREEN = "26, 184, 124"      # 磷绿 #1AB87C 的 RGB
BAND_START = "58%"          # 色带起始高度：越大越靠下
BAND_OPACITY = "0.28"       # 色带浓度：越大越实
INK = "#0E1116"             # 标题墨黑

HL_SPAN_OPEN = (
    f'<span style="background: linear-gradient(transparent {BAND_START}, '
    f'rgba({GREEN}, {BAND_OPACITY}) 0); padding: 0 2px;">'
)
HL_MARKER = f"linear-gradient(transparent {BAND_START}"  # 幂等检测标记

H2_STYLE = (
    "margin: 2.2em 0 1em; font-size: calc(16px * 1.35); font-weight: bold; "
    f"color: {INK}; line-height: 1.5; letter-spacing: 0.02em;"
)

H2_RE = re.compile(r'<h2\b([^>]*)>(.*?)</h2>', re.DOTALL)


def rewrite_h2(open_attrs: str, inner: str) -> str:
    if HL_MARKER in open_attrs or HL_MARKER in inner:
        # 已处理过，原样返回（重建完整标签）
        return f'<h2{open_attrs}>{inner}</h2>'
    # 保留 class / data-heading 等非 style 属性，只换掉 style
    attrs = re.sub(r'\s*style="[^"]*"', '', open_attrs).rstrip()
    return f'<h2{attrs} style="{H2_STYLE}">{HL_SPAN_OPEN}{inner.strip()}</span></h2>'


def convert(html: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        out = rewrite_h2(m.group(1), m.group(2))
        if HL_MARKER not in m.group(1) and HL_MARKER not in m.group(2):
            count += 1
        return out

    return H2_RE.sub(repl, html), count


def main():
    if len(sys.argv) != 2:
        sys.exit("用法: wechat-style-h2.py <article.html>")
    path = Path(sys.argv[1])
    if not path.exists():
        sys.exit(f"找不到文件: {path}")
    src = path.read_text()
    out, n = convert(src)
    if n == 0:
        print("没有需要改写的 H2（可能已处理过或文中无 H2）。")
        return
    backup = path.with_name(f"{path.name}.bak-{datetime.now():%Y%m%d%H%M%S}")
    backup.write_text(src)
    path.write_text(out)
    print(f"✓ 改写 {n} 个 H2 → 荧光笔 A 档（墨黑标题 + 下半段磷绿色带）")
    print(f"  备份: {backup.name}")


if __name__ == "__main__":
    main()
