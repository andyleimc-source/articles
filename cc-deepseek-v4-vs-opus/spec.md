# 文章选题 & 实战横评：CC + DeepSeek V4 vs CC + Opus 4.7

## Context

**为什么写**：DeepSeek V4 Preview（2026-04-24 发布）SWE-bench Verified 80.6，与 Opus 4.7 的 80.8 纸面打平，价格只有后者约 1/30。中英文社区已有大量"我省了 17x"爽文和榜单搬运，**但没人做过同 repo 同 prompt 的严格对照**——这正是 Andy 的「雷码工坊笔记」该补的洞。

**目标读者**：日常用 Claude Code（Opus/Sonnet）做开发的用户，正在纠结"省钱方案能不能干活"。

**输出物**：
- `cc-deepseek-v4-vs-opus/article.md`（中文，公众号主发）
- `cc-deepseek-v4-vs-opus/article-en.md`（英文）
- `cover.svg` + 正文配图（baoyu skills 出图）
- `promotion.md`（多渠道推广）+ `xhs.md`（小红书图卡发布包，若做图卡）

**文章核心问题**（标题方向，非定稿）：
> "SWE-bench 打平、价格 1/30——那 DeepSeek V4 到底能不能替我日常 CC 工作？"

回答方式：用真实 PR 复现做实证对照，给出"何时能切 / 何时别切 / 已知坑"的可操作结论。

---

## 一、测评协议

### 1.1 任务设计（方案 B：真实 merged PR 复现）

**目标 PR 筛选标准**（执行阶段挑选 1 个，写完候选清单先让用户确认）：
- **难度**：中等。PR diff 涉及 3-10 文件、~100-300 LOC
- **领域**：Python 或 TypeScript 中型开源库（避免大型 monorepo / 复杂构建）
- **类型**：feature 或 中等 bug fix（避免纯重构、纯文档）
- **新鲜度**：merge 时间 ≥ 2025-10（避免落入 DeepSeek V4 / Opus 4.7 训练集）
- **完整性**：issue 描述清楚 + 有 reference PR + 有测试可跑
- **自包含**：无外部 service / DB 依赖，`uv sync` 或 `pnpm i` 就能跑测试

**候选搜索路径**：先翻 `httpie/cli`、`charmbracelet/*`、`encode/httpx`、`tiangolo/typer` 之类口碑稳定的库的近期 PR。

**任务执行流程**（每个工具各跑一次）：
1. 从 PR 的 base commit 全新 `git clone`
2. 给 CC 同一份输入：issue 原文 + 一句"修复 / 实现这个，跑通现有测试"
3. CC 自主探索代码 → 修改 → 跑测试 → 收敛
4. 上限：30 turns 或 60 分钟，先到为准

### 1.2 记录指标

| 类别 | 指标 |
|---|---|
| **效果** | ① 测试通过率（reference PR 测试套件 + 新加测试）<br>② 与 reference diff 的语义重合度（人工 + 用 `git diff --stat` 量化）<br>③ 引入的额外改动 / 误删 |
| **成本** | ④ 总 token（input/output/cache 分开）<br>⑤ 等价美元（按官方 list price）<br>⑥ wall-clock 总耗时 |
| **过程** | ⑦ Turn 数<br>⑧ 工具调用次数（Read/Edit/Bash 分类）<br>⑨ 失败重试次数（工具报错、模型纠错） |
| **体感** | ⑩ 主观评分（1-5）：思路清晰度 / 代码风格 / 自纠错能力 |

### 1.3 公平性控制（防被读者质疑"作者偏袒"）

- **同一 prompt** 灌给两个工具，逐字相同
- **顺序随机化**：抛硬币决定先跑哪个；间隔 ≥ 30 分钟避免 CPU 热节流
- **同任务跑两次**：每个工具对每个任务独立跑两轮，取均值（成本可承受时；若任务过长，退化为只第二轮取数）
- **不在 prompt 里暗示"答案"**：只给 issue 原文 + reference PR 的存在但**不给 link**
- **失败也照实记**：工具卡死 / 死循环 / 跑挂测试都如实写进结果表

---

## 二、环境隔离方案

### 2.1 总原则
**用户给出的硬约束**：
- 跑在本机 air
- **最小限度影响日常 CC 配置**（`~/.claude/` 不能被污染）
- 测完**完全恢复原状**，DeepSeek 侧的所有产物全部删除

### 2.2 隔离实施

| 维度 | CC 原生 (Opus 4.7) | CC + DeepSeek V4 |
|---|---|---|
| 机器 | air（本机） | air（本机，**同机**） |
| CC 配置目录 | 用户日常 `~/.claude/` | `CLAUDE_CONFIG_DIR=/tmp/cc-bench-ds/.claude/`（全新空目录，**不导入任何 memory / skill / MCP**） |
| 工作目录 | `/tmp/cc-bench-opus/<repo>/`（全新 clone） | `/tmp/cc-bench-ds/<repo>/`（全新 clone） |
| API 后端 | 用户已配的 Anthropic key | claude-code-router 拦截 → DeepSeek V4 API |
| 录制 | asciinema 全程 + 关键截图 | 同左 |

**配置目录隔离的具体方法**（执行前需验证）：
- 首选：CC 支持 `CLAUDE_CONFIG_DIR` 环境变量（待验证；如不支持则用 `HOME=/tmp/cc-bench-ds zsh -c '...'` 隔离）
- 验证命令：`CLAUDE_CONFIG_DIR=/tmp/test-isolation claude /status` 看是否使用了新目录
- 若两种都不行，回退方案：临时把 `~/.claude/` 重命名为 `~/.claude.bak`，跑完再换回（**风险更高，备选**）

### 2.3 不可控变量及缓解

| 变量 | 缓解 |
|---|---|
| CPU 热节流（连跑两轮第二轮变慢） | 跑完一个任务**强制停 30 分钟**再跑下一个；用 `pmset` 或活动监视器记录 thermal state |
| API 端的限流 / 排队 | 错峰跑（DeepSeek 在中国时段，Anthropic 在美国时段） |
| 模型在线随机性 | 每个任务跑两轮，取均值；记录 raw 数据让读者自己判断 |
| 用户 `~/.gitconfig`（commit author） | 共用无害 |

### 2.4 完全清理 checklist（测评结束后执行）

- [ ] `rm -rf /tmp/cc-bench-opus /tmp/cc-bench-ds`（删工作目录 + 隔离 CC 配置）
- [ ] `claude-code-router` 卸载（`npm uninstall -g` / 删 binary）
- [ ] DeepSeek API key 从环境变量 / keychain 中移除（若临时存过）
- [ ] 检查 `~/.claude/` 完整未变（diff 测试前的备份）
- [ ] 检查 `~/.zshrc` / shell 配置未被改动
- [ ] 删除 router 配置文件（如 `~/.config/claude-code-router/`）
- [ ] 关闭 asciinema 录制文件之外的中间产物（保留录制供文章插图使用）

**测评开始前**：`tar -czf ~/cc-config-backup-$(date +%F).tgz ~/.claude/`，存到 Desktop 或 iCloud，作为"出问题能恢复"的兜底。

---

## 三、执行流程（高层）

每个阶段完成后**等用户审核**再进下一步：

```
[Step 1] 候选 PR 调研  → 列出 3-5 个候选 PR + 推荐 → 用户挑 1 个
[Step 2] 环境搭建      → 装 router + 配 API key + 隔离 CC 配置 + 验证两边都能跑通 hello world
[Step 3] 试跑 + 校准    → 在一个琐碎任务上各跑一次，确认指标采集脚本可用
[Step 4] 正式跑测       → 抛硬币定顺序 → 跑 → 间隔 30min → 跑另一边 → （可选）跑第二轮
[Step 5] 数据分析 + 写文 → 整理 A/B 表 + diff 对比 + 体感叙事
[Step 6] 配图（baoyu skills）→ cover + 正文图（按 BRAND.md 品牌色 + Notion 风格）
[Step 7] humanizer-zh 去 AI 味 → 终稿
[Step 8] 推广文案 promotion.md + xhs.md（如做图卡）
[Step 9] 用户审核终稿 → 发布（公众号 / 知乎 / 小红书 / Twitter）
[Step 10] 环境清理      → 按 §2.4 checklist 执行
```

---

## 四、关键风险

1. **router 对 V4 的兼容度未知**：V4-Pro 当前**纯文本**，发图变占位符——任务设计必须避开图片输入；同时要在 router 配置层验证 tool use schema 是否完全兼容
2. **PR 选错**：太简单两边都满分（无信息量），太难两边都翻车（也无信息量）。Step 1 候选清单要让用户参与挑
3. **DeepSeek V4 服务波动**：刚发布两周，API 稳定性存疑。需要预留"切到 OpenRouter 转发"的备选
4. **token 计数公平性**：CC 客户端的 `/cost` 在 router 模式下可能不准。需要从 router 日志 + DeepSeek 后台用量两侧对账
5. **CC 配置隔离失败**：若 `CLAUDE_CONFIG_DIR` 不被识别，必须在 Step 2 就发现并切换方案，绝不能在污染日常配置后才发现

---

## 五、验证方式（每步完成后怎么自查）

| Step | 验证 |
|---|---|
| 2 | 在隔离目录起 CC，`/status` 显示 config 路径是 `/tmp/cc-bench-ds/.claude/`；用户日常 CC 起来后 memory/skill 全在 |
| 2 | router 起来后，`curl` 一个简单 chat 请求能命中 DeepSeek V4 |
| 3 | 试跑任务两边都能正常完成；指标采集脚本能输出完整 JSON |
| 4 | 每轮跑完，原始 transcript + 录制文件 + 指标 JSON 都已落盘 |
| 5 | A/B 表所有指标有数；对照 reference PR 的 diff 已生成 |
| 10 | `diff -r ~/.claude/ <备份>` 应只差 log/cache 这类自然变化；`which claude-code-router` 应 not found；`/tmp/cc-bench-*` 应不存在 |

---

## 六、关键文件路径

测评开始后产出（待创建）：
- `/Users/andy/Desktop/articles/cc-deepseek-v4-vs-opus/spec.md` — 本 plan 的 article-repo 副本（提交进 git）
- `/Users/andy/Desktop/articles/cc-deepseek-v4-vs-opus/bench/` — 原始 transcript / 录制 / 指标 JSON
- `/Users/andy/Desktop/articles/cc-deepseek-v4-vs-opus/article.md` — 中文终稿
- `/Users/andy/Desktop/articles/cc-deepseek-v4-vs-opus/article-en.md` — 英文版
- `/Users/andy/Desktop/articles/cc-deepseek-v4-vs-opus/promotion.md` — 推广文案（不推 GitHub）

参考既有规则文件（不要修改）：
- `/Users/andy/Desktop/articles/CLAUDE.md` — 项目硬约束
- `/Users/andy/Desktop/articles/WRITING.md` — 写作风格规范
- `/Users/andy/Desktop/articles/BRAND.md` — 品牌色（v2 终端磷绿）
