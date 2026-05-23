#!/usr/bin/env bash
# 一行入口：扫今天 + 渲染 HTML + 自动弹浏览器
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE="${1:-$(TZ=Asia/Shanghai date +%F)}"

# 支持 ./scan.sh --date 2026-05-17 这种调用
if [[ "${1:-}" == "--date" ]]; then DATE="${2:-$DATE}"; fi

cd "$DIR"
mkdir -p data/candidates data/logs

LOG="data/logs/${DATE}.log"
echo "=== scan @ $(date '+%F %T') ===" | tee -a "$LOG"

python3 scripts/scan.py --date "$DATE" 2>&1 | tee -a "$LOG"
python3 scripts/render_html.py --date "$DATE" 2>&1 | tee -a "$LOG"

HTML="data/candidates/${DATE}.html"
if [[ -f "$HTML" ]]; then
  echo "[scan.sh] 打开 $HTML"
  open "$HTML" || true
else
  echo "[scan.sh] HTML 没生成，看 $LOG"
fi
