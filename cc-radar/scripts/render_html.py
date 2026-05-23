#!/usr/bin/env python3
"""把 data/candidates/<date>.json 渲染成单文件 HTML，浏览器直接打开看。"""
import argparse
import html
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAND_DIR = ROOT / "data" / "candidates"

BRAND = {
    "bg": "#FAF7F0",
    "ink": "#0E1116",
    "green": "#1AB87C",
    "graphite": "#3A4151",
    "fog": "#9CB4CC",
    "brick": "#6E6259",
}


def today_str() -> str:
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")


def render(date_str: str, data: dict) -> str:
    cands = data.get("candidates", [])
    note = data.get("note", "")
    total = data.get("total_hits", 0)
    after = data.get("after_dedup", 0)
    threshold = data.get("threshold", 70)

    cards = []
    if not cands:
        cards.append(
            f"""<div class="empty">
            <h2>今天没命中</h2>
            <p>关键词命中：{total} 条 / 去重后：{after} 条 / 过阈值（≥{threshold}）：0 条</p>
            <p>{html.escape(note)}</p>
          </div>"""
        )
    else:
        for c in cands:
            cmd = f"./cc-radar/scripts/evaluate.sh {c['id']}"
            cards.append(
                f"""<div class="card">
            <div class="head">
              <span class="score">{c['score']}</span>
              <span class="feat">{html.escape(c['cc_feature_name'])}</span>
              <span class="meta">@{html.escape(c['author'])} · <a href="{html.escape(c['source_url'])}" target="_blank">原推</a></span>
            </div>
            <div class="summary">{html.escape(c['summary'])}</div>
            <div class="why"><b>值得测：</b>{html.escape(c['why_worth_testing'])}</div>
            <div class="demo"><b>建议 demo：</b>{html.escape(c['suggested_demo'])}</div>
            <div class="raw"><details><summary>原文</summary><pre>{html.escape(c['raw_text'])}</pre></details></div>
            <div class="cmd">
              <code id="cmd-{c['id']}">{html.escape(cmd)}</code>
              <button onclick="copyCmd('cmd-{c['id']}', this)">复制</button>
            </div>
          </div>"""
            )

    return f"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>cc-radar 候选 · {date_str}</title>
<style>
  body {{ background:{BRAND['bg']}; color:{BRAND['ink']}; font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Helvetica Neue",sans-serif; margin:0; padding:32px; }}
  h1 {{ color:{BRAND['ink']}; margin:0 0 8px; }}
  .sub {{ color:{BRAND['graphite']}; margin:0 0 24px; font-size:14px; }}
  .card {{ background:#fff; border:1px solid {BRAND['fog']}33; border-radius:10px; padding:20px; margin:16px 0; box-shadow:0 1px 2px {BRAND['brick']}11; }}
  .head {{ display:flex; align-items:center; gap:12px; margin-bottom:8px; }}
  .score {{ background:{BRAND['green']}; color:#fff; padding:2px 10px; border-radius:6px; font-weight:600; font-size:14px; }}
  .feat {{ font-weight:600; color:{BRAND['ink']}; font-size:18px; }}
  .meta {{ color:{BRAND['graphite']}; font-size:13px; margin-left:auto; }}
  .meta a {{ color:{BRAND['green']}; text-decoration:none; }}
  .summary {{ color:{BRAND['ink']}; margin:10px 0; font-size:15px; line-height:1.6; }}
  .why, .demo {{ color:{BRAND['graphite']}; font-size:13px; margin:4px 0; line-height:1.5; }}
  .why b, .demo b {{ color:{BRAND['green']}; }}
  .raw {{ margin:10px 0; font-size:12px; color:{BRAND['brick']}; }}
  .raw pre {{ background:{BRAND['bg']}; padding:10px; border-radius:6px; white-space:pre-wrap; word-break:break-word; font-family:"SF Mono",Menlo,monospace; }}
  .cmd {{ display:flex; align-items:center; gap:8px; background:{BRAND['ink']}; color:#fff; padding:10px 12px; border-radius:6px; margin-top:12px; }}
  .cmd code {{ flex:1; font-family:"SF Mono",Menlo,monospace; font-size:13px; }}
  .cmd button {{ background:{BRAND['green']}; color:#fff; border:0; padding:6px 12px; border-radius:4px; cursor:pointer; font-size:13px; }}
  .cmd button:hover {{ opacity:0.85; }}
  .empty {{ text-align:center; padding:60px 20px; color:{BRAND['graphite']}; }}
  .empty h2 {{ color:{BRAND['ink']}; }}
  .footer {{ color:{BRAND['brick']}; font-size:12px; margin-top:32px; text-align:center; }}
</style>
</head>
<body>
  <h1>cc-radar · {date_str}</h1>
  <p class="sub">关键词命中 {total} · 去重后 {after} · 过阈值（≥{threshold}）{len(cands)}</p>
  {''.join(cards)}
  <p class="footer">复制命令 → 终端粘贴运行 → 自动跑测评</p>
<script>
function copyCmd(id, btn) {{
  const t = document.getElementById(id).innerText;
  navigator.clipboard.writeText(t).then(() => {{
    btn.innerText = '已复制';
    setTimeout(() => btn.innerText = '复制', 1500);
  }});
}}
</script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today_str())
    args = ap.parse_args()
    jpath = CAND_DIR / f"{args.date}.json"
    if not jpath.exists():
        print(f"[error] {jpath} 不存在；先跑 scan.py", file=sys.stderr)
        return 1
    data = json.loads(jpath.read_text(encoding="utf-8"))
    out = CAND_DIR / f"{args.date}.html"
    out.write_text(render(args.date, data), encoding="utf-8")
    print(f"[render] {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
