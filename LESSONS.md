# LESSONS.md

## Markdown 转 docx（pandoc）

### 问题：图片不显示
- **原因**：文章里用的是 HTML `<img src="...">` 标签，pandoc 默认不嵌入 HTML img 标签中的图片。
- **解法**：转换前用 Python 把 `<img src="路径" height="...">` 替换为标准 markdown 语法 `![](路径){height=Xcm}`，同时用 `urllib.parse.unquote` 解码路径中的 URL 编码（如 `%20` → 空格）。
- **注意**：pandoc 必须在文章目录下运行，否则相对路径 `image/xxx` 找不到图片。

### 问题：图片尺寸不受控
- **原因**：pandoc 转 docx 时忽略 `height` 属性，图片按原始尺寸嵌入。
- **解法**：在 markdown 图片语法后加 pandoc 属性 `{height=8cm}`，高度 8cm 约对应屏幕显示 300px 的视觉效果。
- **单位换算参考**：3cm ≈ 113px，8cm ≈ 300px（96dpi 基准）。

### 完整转换命令模板
```python
import re, urllib.parse

with open('article.md', 'r') as f:
    content = f.read()

def replace_img(m):
    src = urllib.parse.unquote(m.group(1))
    return f'![]({src}){{height=8cm}}'

content2 = re.sub(r'<img src="([^"]+)"[^/]*/>', replace_img, content)

with open('article_tmp.md', 'w') as f:
    f.write(content2)
```
然后在文章目录下运行：
```bash
pandoc article_tmp.md -o output.docx --from markdown --to docx && rm article_tmp.md
```
