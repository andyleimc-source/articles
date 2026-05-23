#!/usr/bin/env bash
# 一行入口：./cc-radar/scripts/evaluate.sh 2026-04-28-01
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/.."  # 项目根
exec python3 "$DIR/scripts/evaluate.py" "$@"
