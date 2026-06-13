#!/usr/bin/env python3
"""
把 articles 仓库的 article.md 转成公众号脚本能正确识别的格式。

转换规则：
- 顶部 cover `<img src="cover.png">`：保留（封面手动上传）
- 正文 `<img src="image/xxx" height="300">` + 紧跟的 `<p align="center"><em>caption</em></p>`：
  转成
      ![](image/xxx)

      <p align="center"><em>caption</em></p>
  注意：图片必须是 markdown `![](path)` 才会被公众号脚本识别；caption 必须保留为
  独立的 HTML 段落（不能塞进 alt 文本，alt 在公众号不渲染）。

用法：
    ./scripts/md-to-wechat.py <article-dir>/article.md
    输出：<article-dir>/article-wechat.md
"""
import re
import sys
from pathlib import Path

CAPTION_STYLE = "text-align:center;color:#888;font-size:14px;font-style:italic;margin-top:-0.5em;"

def convert(src: str) -> tuple[str, int]:
    """
    转换规则（2026-05-18 修复，踩雷见 [[feedback-wechat-caption-alt-pitfall]]）：
    - <img height=300> + <p align="center"><em>caption</em></p>
      → ![](path)
        <section style="...">caption</section>
    用 <section> 而不是 <p align="center">：后者会让 ProseMirror 把图片段落和 caption 段落
    认成同一个 block，粘贴图片时图片会被 "吃" 掉（2026-05-18 实测）。<section> 是不透明
    block 元素，ProseMirror 不会试图合并。
    """
    pattern = re.compile(
        r'<img src="(image/[^"]+)"[^>]*>\s*\n<p align="center"><em>(.+?)</em></p>'
    )
    matches = pattern.findall(src)
    out = pattern.sub(
        lambda m: f'![]({m.group(1)})\n\n<section style="{CAPTION_STYLE}">{m.group(2)}</section>',
        src,
    )
    return out, len(matches)

def main():
    if len(sys.argv) != 2:
        sys.exit("用法: md-to-wechat.py <article.md>")
    src_path = Path(sys.argv[1])
    if not src_path.exists():
        sys.exit(f"找不到文件: {src_path}")
    out_path = src_path.with_name("article-wechat.md")
    converted, n = convert(src_path.read_text())
    out_path.write_text(converted)
    print(f"✓ 转换 {n} 张图片+caption → {out_path}")
    print(f"  下一步: cd {src_path.parent} && npx -y bun .../wechat-article.ts --markdown article-wechat.md ...")

if __name__ == "__main__":
    main()
