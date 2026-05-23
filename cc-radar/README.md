# cc-radar

从 [xradar](https://github.com/andyleimc-source/xradar) 每日抓到的推文里，自动筛出 Claude Code 功能相关的，由 Claude 自己跑 demo + 写测评草稿。

## 工作流

```
xradar cron(远程) → rsync 本地 → scan.sh → 候选 HTML → 你勾选 → evaluate.sh → cc-<slug>/ 草稿
```

## 用法

```bash
# 1) 扫今天（东八区）。也可以 ./cc-radar/scripts/scan.sh 2026-04-28 跑历史
./cc-radar/scripts/scan.sh

# 2) 浏览器会自动弹 cc-radar/data/candidates/<date>.html
#    每张卡片底下有一行命令，按「复制」→ 贴回终端跑：
./cc-radar/scripts/evaluate.sh 2026-MM-DD-01

# 3) 跑完会在项目根新建 cc-<feature-slug>/，里面有：
#    - SOURCE.md         候选元信息
#    - article.md        Claude 写好的草稿
#    - demo/*.log        实测终端输出
#    - cover-prompt.md   下一步出封面的 prompt
#    然后手动：
#       cd cc-<slug>
#       Skill baoyu-cover-image  # 出 cover.png
#       Skill humanizer-zh        # 去 AI 味
```

## 关键文件

- `config.yaml` — 白名单账号 / 关键词 / 阈值
- `prompts/select.md` — DeepSeek 打分 prompt
- `prompts/evaluate.md` — claude -p 测评 prompt
- `data/` — 候选 / 日志 / history（**不入 git**）

## 调试 flag

```bash
python3 cc-radar/scripts/scan.py --no-llm           # 跳过 DeepSeek，看关键词命中
python3 cc-radar/scripts/scan.py --ignore-history   # 不去重（回放历史）
python3 cc-radar/scripts/scan.py --raw-dir /tmp/x   # 测试用 fixture
python3 cc-radar/scripts/evaluate.py 2026-MM-DD-NN --dry-run  # 只建脚手架
python3 cc-radar/scripts/evaluate.py 2026-MM-DD-NN --step claude  # 只重跑 claude
```

## 定时（macOS launchd）

每日 09:00 跑 scan：

```bash
cp cc-radar/launchd/com.andy.cc-radar.scan.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.andy.cc-radar.scan.plist
launchctl start com.andy.cc-radar.scan
```

xradar 远程 cron 是 06:00（东八），留 3h 给 rsync 同步。

## 依赖

- Python 3.10+（系统 Python 即可，无外部包）
- `claude` CLI（`evaluate.sh` 用）
- xradar 本地有数据（`/Users/andy/Documents/running/xradar/data/raw/`）
- xradar `.env` 里有 `DEEPSEEK_API_KEY`（scan 调 DeepSeek 用）

## 已知限制

- `claude -p` headless 跑长链路任务可能偏题或超时——用 `--step claude` 重跑
- demo 截图：CC 没原生截图能力，只存终端日志；要图自己用 aha / Chrome headless 后期补
- humanizer-zh 跑后仍需老雷过叙事质量
