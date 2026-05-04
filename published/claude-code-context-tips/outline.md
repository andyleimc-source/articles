---
topic: Claude Code 上下文管理最佳实践
slug: claude-code-context-tips
style: notion
palette: default
language: zh-CN
count: 5
watermark: 雷码工坊笔记
strategy: B — Information-Dense
---

# 图文大纲

## 01 封面 · sparse
- 主标题：Claude Code 越聊越慢？
- 副标题：上下文这个坑，很多人不知道
- 钩子：长会话 = 高额度 + 低质量
- 视觉：终端窗口涂鸦 + 百分比条进入红色区

## 02 核心原理 · balanced
- 标题：LLM 是无状态的
- 要点：
  - 每句新消息都要把**整段历史**重新发给模型
  - 会话越长 → token 越多 → 越慢越贵
  - Prompt Cache 5 分钟 TTL：连续聊便宜，断线就失效
- 视觉：左边"你"的简笔 + 右边模型盒子 + 不断加粗的消息流

## 03 上下文阈值指南 · list
- 标题：到多少该切会话？
- 4 档清单：
  - < 50%：放心聊（绿）
  - 50–70%：任务收尾就 /clear（黄）
  - 70–80%：主动切会话、写 handoff（橙）
  - > 80%：必须切！auto-compact 会丢细节（红）
- 视觉：竖向温度计 / 油量表

## 04 恢复历史会话的坑 · comparison
- 标题：Resume 时别点错按钮
- 左栏（❌）：Resume full session as-is
  - 一次性加载全部历史
  - 冷启动 + 无缓存
  - 瞬间吃掉用量配额
- 右栏（✅）：Resume from summary
  - 先压缩成摘要再恢复
  - 上下文小，省 token
  - 推荐默认选项
- 视觉：两扇门 / 两条分岔

## 05 最佳实践四件套 · list
- 标题：长期可持续的用法
- 4 条清单：
  - CLAUDE.md 项目约定（永久）
  - Progress.md 进展记录（每个里程碑）
  - handoff.md 交接文档（切会话前）
  - 任务告一段落立刻 /clear
- 底部 CTA：关注「雷码工坊笔记」
- 视觉：4 个文件图标排列 + 右下角 /clear 命令高亮
