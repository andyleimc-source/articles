#!/bin/bash
# md2docx.sh — 将 Markdown 文章转为 Word (.docx)
# 用法: ./md2docx.sh <markdown文件路径>
# 示例: ./md2docx.sh publish/why-claude-code-doesnt-flatter-you/article-cn.md

set -euo pipefail

if [ $# -eq 0 ]; then
  echo "用法: $0 <markdown文件路径>"
  echo "示例: $0 publish/why-claude-code-doesnt-flatter-you/article-cn.md"
  exit 1
fi

INPUT="$1"

if [ ! -f "$INPUT" ]; then
  echo "错误: 文件不存在: $INPUT"
  exit 1
fi

# 输出文件：同目录，同名但扩展名改为 .docx
OUTPUT="${INPUT%.md}.docx"

# 脚本所在目录（用于定位 Lua filter）
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 获取输入文件所在目录，用于解析相对路径的图片
INPUT_DIR="$(cd "$(dirname "$INPUT")" && pwd)"
INPUT_BASENAME="$(basename "$INPUT")"

echo "转换中: $INPUT → $OUTPUT"

# 使用 pandoc 转换
# --resource-path: 设置图片等资源的搜索路径
# --wrap=none: 不自动换行
# -f markdown+raw_html: 支持 HTML 标签（如 <img>）
cd "$INPUT_DIR"
pandoc "$INPUT_BASENAME" \
  -f markdown+raw_html \
  --lua-filter="$SCRIPT_DIR/img-filter.lua" \
  --resource-path="$INPUT_DIR" \
  --wrap=none \
  -o "$(basename "$OUTPUT")"

if [ $? -eq 0 ]; then
  echo "完成: $OUTPUT"
else
  echo "转换失败"
  exit 1
fi
