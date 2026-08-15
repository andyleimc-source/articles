# AGENTS.md — agy（Antigravity/Gemini）等施工方 CLI 在本项目的入口（薄壳）

> 单一真相源 = `./CLAUDE.md`（项目规则正本）。本文件不复制内容，只定角色和差异。

**第一步：完整读 `./CLAUDE.md`**，项目规则以它为准。同时遵守全局 `~/.claude/CLAUDE.md`（协作偏好、bye 落盘等）。读到你执行不了的机制时按下表处理：

## 忽略清单（Claude Code 专属，你无法执行，跳过即可）

- Claude 的记忆系统（`~/.claude/projects/.../memory/`）、子代理（Agent/Task 委派）、会话内 TaskCreate 待办
- SessionStart hook 注入的专属上下文机制、`statusLine`
- Skill / slash 命令触发词——本项目 `.claude/skills/` 你不一定读得到，读不到就说没有，别假装调得到

## 照做清单（与 Claude 同一标准）

- **生成的文件 / skill 一律落在本项目内，禁止碰 `~/dotfiles` 或任何全局 skills 目录**，除非 Andy 明确要求跨机器共享
- 花钱动作（LLM/搜索 API、云资源）执行前必须向用户确认
- 不确定直说不确定，不要猜；语音输入有错别字，按上下文理解纠正

⚠ 非交互（`-p`/print）模式下默认没有工作区，读不到本文件——调用时必须带 `--add-dir <本项目绝对路径>`。
