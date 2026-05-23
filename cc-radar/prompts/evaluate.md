# Claude Code 功能测评任务

你被 cc-radar 自动调起，来给一个 Claude Code 功能写测评草稿。

## 你的目标

读 `SOURCE.md`，理解这个候选讲的是 Claude Code 的什么功能，然后：

1. **实测**——用 Bash 工具跑命令验证这个功能（尽量在当前目录或 `/tmp/cc-radar-eval/` 下，不污染外部）。
   - 如果是 CLI 功能：直接 `claude --help`、`claude -p "..."` 等命令验证
   - 如果是 hook / skill / MCP：在 `.claude/` 下临时建配置跑一次
   - **重要**：把所有终端输出存到 `demo/<step>-<name>.log`（例如 `demo/01-help-output.log`、`demo/02-run-feature.log`），后续 caption / 截图基于这些日志
   - 如果某步跑不通（功能不存在 / 文档过期 / 需要付费版），如实记录在 `demo/00-blockers.md`，不要硬编

2. **写草稿** `article.md`，严格按 WRITING.md 的"功能测评"风格（不是叙事文）：
   - 顶部用 `<img src="cover.png">` 占位（封面后续生成）
   - 大致结构：钩子（一句话讲为什么这个功能值得知道）/ 这是什么 / 怎么用（最关键，含 demo 输出节选）/ 我在哪卡住了 / 给读者的建议 / 一句话总结
   - 长度：800-1500 中文字
   - 引用 demo log 时贴关键片段（10-30 行），不要全文塞
   - 外链给全地址（不要只放 `[xxx](url)`）
   - 标题加粗用磷绿（H2/H3 用 `##`/`###`，强调用 `**...**`）

3. **不要做**的事：
   - 不要跑 humanizer-zh（脚本会自动跑）
   - 不要出封面图（脚本会调 baoyu-cover-image）
   - 不要 commit（脚本会一起 commit）
   - 不要修改 cc-radar/ 目录下任何文件
   - 不要读其他文章作参考（CLAUDE.md 硬规则）

## 输入

- `SOURCE.md`：候选元信息（功能名 / 摘要 / 原推链接 / 建议 demo）
- `article.md`：已有 outline 骨架，你**直接编辑**这个文件填充内容
- 项目根 `/Users/andy/Desktop/articles/WRITING.md`：写作规范（你已经有 add-dir 权限）

## 完成标志

`article.md` 写完 + `demo/` 目录至少有 1 个有内容的 log 文件 + 没有未保存的草稿。完成后直接结束，不要等用户确认。
