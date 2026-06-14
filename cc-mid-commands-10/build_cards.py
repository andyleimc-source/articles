#!/usr/bin/env python3
"""渲染 Claude Code 进阶 10 命令图卡系列（HTML→PNG，文字零错误）。
复刻 published/10-claude-code-tips 视觉系统：米白点阵纸 + 黑色线稿 + 黄色荧光笔强调。
用法：python3 build_cards.py            # 全部 12 张
      python3 build_cards.py --only 02 # 只渲染某张
"""
import html, subprocess, sys, tempfile, os, pathlib

BASE = pathlib.Path(__file__).resolve().parent
IMG = BASE / "image"
IMG.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TOTAL_PAGES = 12  # 封面 + 10 + 结尾

# ---------------- 卡片数据 ----------------
CARDS = [
    {"id": "01", "type": "cover", "file": "01-cover",
     "badge": "进阶必学", "title_en": "Claude Code", "title_zh": "10 个中级命令",
     "hook": "老手也未必全会 👀"},

    {"id": "02", "type": "tip", "file": "02-goal", "n": 1, "cmd": "/goal",
     "subtitle": "目标达成前，它不停手",
     "principle": "给一个完成条件，每跑完一轮自动检查，没达成就继续改，直到满足或你喊停。",
     "code": ["/goal 所有测试通过"],
     "takeaway": "AI 反复改代码跑测试，绿了才停",
     "tagline": "自己干到底 ✓"},

    {"id": "03", "type": "tip", "file": "03-rewind", "n": 2, "cmd": "/rewind",
     "subtitle": "改崩了的后悔药",
     "principle": "每次文件改动和每轮对话都存了本地快照，一句命令就能把代码和对话一起退回任意一步。",
     "code": ["/rewind", "→ 选「重构之前」检查点"],
     "takeaway": "改崩的文件一键还原，不用翻 git",
     "tagline": "大胆试，反正能回去 ✓"},

    {"id": "04", "type": "tip", "file": "04-context", "n": 3, "cmd": "/context",
     "subtitle": "看清 token 都被谁吃了",
     "principle": "把当前上下文按来源拆成彩色网格，CLAUDE.md、对话、工具、记忆各占多少一目了然，还给优化建议。",
     "code": ["/context", "→ MCP 工具定义吃了 30%"],
     "takeaway": "关掉用不上的，腾出空间",
     "tagline": "省 token，先看钱花哪"},

    {"id": "05", "type": "tip", "file": "05-memory", "n": 4, "cmd": "/memory",
     "subtitle": "管 AI 的长期记忆",
     "principle": "一个入口编辑各层级 CLAUDE.md、开关自动记忆，还能审计 AI 到底记了你项目的什么。",
     "code": ["/memory", "→ 编辑项目 CLAUDE.md", "→ 查看 AI 自动记的条目"],
     "takeaway": "记错的当场删，规矩当场补",
     "tagline": "AI 记什么，你说了算"},

    {"id": "06", "type": "tip", "file": "06-resume", "n": 5, "cmd": "/resume",
     "subtitle": "找回任何历史会话",
     "principle": "每段会话都存在本地。弹出历史列表按名字挑，或用 -c 直接接上当前目录最近那次，上下文原样还在。",
     "code": ["claude -c     # 接上最近一次", "/resume       # 翻历史挑一段"],
     "takeaway": "昨天聊一半，今天接着干",
     "tagline": "关了终端，思路不丢"},

    {"id": "07", "type": "tip", "file": "07-permissions", "n": 6, "cmd": "/permissions",
     "subtitle": "少弹一半确认框",
     "principle": "给工具设 允许 / 询问 / 拒绝 规则，常用的安全命令加进 allow，直接跑不再每次问，危险操作仍拦你。",
     "code": ["/permissions", "allow: Bash(npm test)", "allow: Bash(git status)"],
     "takeaway": "读类操作不再打断你",
     "tagline": "该放行放行，该兜底兜底"},

    {"id": "08", "type": "tip", "file": "08-agents", "n": 7, "cmd": "/agents",
     "subtitle": "一个人变一个小队",
     "principle": "定义带专属说明的子代理，各有独立上下文窗口。任务匹配上时自动派活，互不污染主线。",
     "code": ["/agents", "→ 建「测试编写」代理", "→ 建「代码审查」代理"],
     "takeaway": "脏活分给分身，主线只推进",
     "tagline": "复杂活，自动分派"},

    {"id": "09", "type": "tip", "file": "09-loop", "n": 8, "cmd": "/loop",
     "subtitle": "让它自己重复跑",
     "principle": "把一个 prompt 按你给的间隔反复执行，盯状态、跑维护任务全自动；不给间隔就让它自己掌握节奏。",
     "code": ["/loop 5m 检查部署状态"],
     "takeaway": "每 5 分钟看一眼，有变化才叫你",
     "tagline": "重复的活，交给循环"},

    {"id": "10", "type": "tip", "file": "10-background", "n": 9, "cmd": "/background",
     "subtitle": "会话挂后台继续干",
     "principle": "把当前会话脱离终端转成后台代理继续跑，终端立刻解放去干别的，回头 /resume 接回来看结果。",
     "code": ["/background", "→ 大重构挂后台跑", "→ 你照常写别的代码"],
     "takeaway": "长任务不占着终端干等",
     "tagline": "让它后台跑，你别干等"},

    {"id": "11", "type": "tip", "file": "11-review", "n": 10, "cmd": "/code-review",
     "subtitle": "云端多代理审代码",
     "principle": "把当前分支的 diff 丢到云端沙箱，多个审查代理并行从 bug、风格、效率多角度过一遍，不占本地上下文。",
     "code": ["/code-review ultra", "→ 多代理并行审当前分支"],
     "takeaway": "合并前先让一队 AI 挑刺",
     "tagline": "合并前，过一队审查官"},

    {"id": "12", "type": "ending", "file": "12-ending",
     "badge": "10 个命令 全部解锁 ✓",
     "title_zh": "收藏这张卡片", "sub": "下次用 Claude Code 更进一步！",
     "cta": "👉 关注获取更多 AI 效率技巧",
     "tags": "#ClaudeCode  #AI效率工具  #程序员必备"},
]

# ---------------- 公共样式 ----------------
CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:900px; height:1200px; overflow:hidden; }
:root{
  --cream:#FAF7F0; --ink:#0E1116; --graphite:#3A4151; --muted:#8C877C;
  --yellow:#FBE08A; --yellowcard:#FBF1C7; --yellowborder:#EFE0A0;
  --graycard:#F1EFEA; --grayborder:#E2DED4; --code:#EAE7E1;
}
body{
  background:var(--cream);
  background-image:radial-gradient(circle, #D9D4C7 1.4px, transparent 1.6px);
  background-size:27px 27px; background-position:6px 6px;
  font-family:"PingFang SC","Source Han Sans CN","思源黑体 CN","Hiragino Sans GB",sans-serif;
  color:var(--ink); position:relative;
}
.wrap{ width:900px; height:1200px; padding:66px 60px 58px; display:flex; flex-direction:column; }
.latin{ font-family:"Arial Black","Helvetica Neue",Arial,sans-serif; }
.mono{ font-family:"SF Mono","Menlo","Consolas",monospace; }

/* badge */
.badge{ align-self:flex-start; background:#E7E4DB; color:var(--ink);
  font-size:25px; font-weight:600; padding:9px 22px; border-radius:11px; }
.badge .slash{ color:var(--muted); font-weight:600; }

/* tip card */
.cmd{ font-size:118px; font-weight:900; letter-spacing:-3px; line-height:1.02;
  margin:26px 0 6px; }
.subtitle{ font-size:46px; font-weight:700; margin-bottom:34px; }
.card{ border-radius:22px; padding:28px 30px 30px; margin-bottom:26px; border:1.5px solid; }
.card.gray{ background:var(--graycard); border-color:var(--grayborder); }
.card.yellow{ background:var(--yellowcard); border-color:var(--yellowborder); }
.card-h{ font-size:31px; font-weight:700; margin-bottom:16px; }
.card-b{ font-size:32px; line-height:1.6; font-weight:500; color:#1B1F26; }
.code{ background:var(--code); border-radius:13px; padding:20px 24px; margin-bottom:16px; }
.code .line{ font-size:29px; line-height:1.55; color:var(--ink); white-space:pre; }
.arrow{ font-size:30px; font-weight:600; color:var(--graphite); }
.spacer{ flex:1; }
.tagline{ text-align:center; font-size:62px; font-weight:900; line-height:1.2; }
.tagline .hl{ background:linear-gradient(transparent 52%, var(--yellow) 52%, var(--yellow) 90%, transparent 90%);
  padding:0 10px; }
.page{ text-align:center; color:#B3AEA2; font-size:27px; margin-top:30px; }
.wm{ position:absolute; right:42px; bottom:34px; color:#6E6259; opacity:.55;
  font-size:22px; font-weight:500; }

/* cover */
.cover-badge{ align-self:center; background:var(--ink); color:#fff; font-size:34px; font-weight:700;
  padding:12px 34px; border-radius:40px; margin-top:18px; }
.cover-en{ font-size:104px; font-weight:900; text-align:center; letter-spacing:-2px; margin-top:40px; line-height:1.05; }
.cover-zh{ font-size:74px; font-weight:900; text-align:center; margin-top:6px; }
.cover-zh .hl{ background:linear-gradient(transparent 54%, var(--yellow) 54%, var(--yellow) 92%, transparent 92%); padding:0 14px; }
.term{ width:560px; height:380px; border:5px solid var(--ink); border-radius:20px; margin:60px auto 0; position:relative; }
.term .bar{ position:absolute; top:22px; left:26px; display:flex; gap:14px; }
.term .bar i{ width:18px; height:18px; border:3px solid var(--ink); border-radius:50%; display:block; }
.term .prompt{ position:absolute; top:130px; left:54px; font-size:70px; font-weight:900; }
.cover-hook{ text-align:center; color:var(--muted); font-size:42px; font-weight:600; margin-top:auto; }

/* ending */
.end-badge{ align-self:center; background:var(--ink); color:#fff; font-size:36px; font-weight:700;
  padding:14px 40px; border-radius:44px; margin-top:6px; }
.laptop{ width:430px; height:300px; margin:54px auto 0; position:relative; }
.laptop .scr{ width:430px; height:270px; border:5px solid var(--ink); border-radius:16px; }
.laptop .base{ width:520px; height:20px; border:5px solid var(--ink); border-radius:0 0 16px 16px;
  margin-left:-45px; border-top:none; }
.laptop .win{ position:absolute; top:70px; left:150px; width:300px; height:190px; border:5px solid var(--ink);
  border-radius:14px; background:var(--cream); }
.laptop .win .p{ position:absolute; top:60px; left:30px; font-size:48px; font-weight:900; }
.end-title{ text-align:center; font-size:96px; font-weight:900; margin-top:64px; }
.end-title .hl{ background:linear-gradient(transparent 52%, var(--yellow) 52%, var(--yellow) 90%, transparent 90%); padding:0 12px; }
.end-sub{ text-align:center; font-size:42px; font-weight:700; margin-top:22px; }
.end-rule{ border:none; border-top:2px solid #D9D4C7; margin:40px 30px 0; }
.end-cta{ text-align:center; font-size:40px; font-weight:700; margin-top:34px; }
.end-tags{ text-align:center; color:var(--muted); font-size:30px; font-weight:600; margin-top:30px; }
"""

def esc(s): return html.escape(s)

def render_tip(c):
    code = "".join(f'<div class="line mono">{esc(l)}</div>' for l in c["code"])
    return f"""
    <div class="wrap">
      <div class="badge">技巧 {c['n']:02d}<span class="slash"> / 10</span></div>
      <div class="cmd latin">{esc(c['cmd'])}</div>
      <div class="subtitle">{esc(c['subtitle'])}</div>
      <div class="card gray">
        <div class="card-h">🧠 运作原理</div>
        <div class="card-b">{esc(c['principle'])}</div>
      </div>
      <div class="card yellow">
        <div class="card-h">📌 案例示范</div>
        <div class="code">{code}</div>
        <div class="arrow">→ {esc(c['takeaway'])}</div>
      </div>
      <div class="spacer"></div>
      <div class="tagline"><span class="hl">{esc(c['tagline'])}</span></div>
      <div class="page">{int(c['id'])} / {TOTAL_PAGES}</div>
    </div>
    <div class="wm">雷码工坊笔记</div>"""

def render_cover(c):
    return f"""
    <div class="wrap">
      <div class="cover-badge">{esc(c['badge'])}</div>
      <div class="cover-en latin">{esc(c['title_en'])}</div>
      <div class="cover-zh"><span class="hl">{esc(c['title_zh'])}</span></div>
      <div class="term"><div class="bar"><i></i><i></i><i></i></div><div class="prompt latin">&gt;_</div></div>
      <div class="cover-hook">{esc(c['hook'])}</div>
    </div>
    <div class="wm">雷码工坊笔记</div>"""

def render_ending(c):
    return f"""
    <div class="wrap">
      <div class="end-badge">{esc(c['badge'])}</div>
      <div class="laptop">
        <div class="scr"></div><div class="base"></div>
        <div class="win"><div class="p latin">&gt;_</div></div>
      </div>
      <div class="end-title"><span class="hl">{esc(c['title_zh'])}</span></div>
      <div class="end-sub">{esc(c['sub'])}</div>
      <hr class="end-rule">
      <div class="end-cta">{esc(c['cta'])}</div>
      <div class="end-tags">{esc(c['tags'])}</div>
    </div>
    <div class="wm">雷码工坊笔记</div>"""

def page_html(c):
    body = {"cover": render_cover, "tip": render_tip, "ending": render_ending}[c["type"]](c)
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"

def render(c):
    out = IMG / f"{c['file']}.png"
    if out.exists():
        import datetime
        # backup rule
        bak = out.with_name(f"{c['file']}-backup.png")
        if not bak.exists(): os.replace(out, bak)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(page_html(c)); tmp = f.name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", "--window-size=900,1200",
        f"--screenshot={out}", f"file://{tmp}"],
        check=True, capture_output=True)
    os.unlink(tmp)
    print(f"✓ {out.name}")

if __name__ == "__main__":
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    for c in CARDS:
        if only and c["id"] != only and c["file"] != only: continue
        render(c)
