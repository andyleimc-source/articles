---
strategy: b
name: Information-Dense
style: notion
style_reason: "Notion 极简风格最适合知识型干货教程，清爽专业"
elements:
  background: solid-white
  decorations: [line-art-icons, dotted-arrows]
  emphasis: underline
  typography: clean-sans
layout: flow
image_count: 6
---

## P1 Cover
**Type**: cover
**Hook**: "Claude Code 国内配置，看这一篇就够了"
**Visual**: 标题居中，下方三个手绘线描图标（钥匙、卡片、终端），用虚线箭头串联
**Layout**: sparse
**Text**: 
- 主标题：Claude Code 国内配置指南
- 副标题：账号 · 支付 · 模型 · 一次搞定

## P2 Content — 账号准备
**Type**: content
**Message**: 两步搞定账号
**Visual**: 两个区块上下排列，手绘图标
**Layout**: list
**Text**:
- 📱 海外手机号：用接码平台，充 2 美元，选小众国家号码
- 🍎 美区苹果账号：第三方平台购买，¥20，稳定好用

## P3 Content — 支付方案
**Type**: content
**Message**: 礼品卡方案最稳
**Visual**: 礼品卡图标 + 充值流程
**Layout**: flow
**Text**:
- 国内信用卡大概率被拒
- 买 Apple / Google Play 礼品卡
- 直接充值，不用绑海外卡
- 前提：需要美区账号（上一步解决了）

## P4 Content — 连接模型
**Type**: content
**Message**: 两条路选一条
**Visual**: 左右对比布局
**Layout**: comparison
**Text**:
- 路线 A：官方订阅（注意封号风险）
- 路线 B：国内 API Key（DeepSeek / MiniMax / 千问 / Kimi）
- Claude Code 只是调用端，换模型照样跑

## P5 Content — 使用技巧
**Type**: content
**Message**: 两个必会技巧
**Visual**: 代码框 + 说明
**Layout**: list
**Text**:
- 技巧1：加 --dangerously-skip-permissions 告别反复授权
- 技巧2：先说"告诉我你打算怎么做"，避免文件被改乱

## P6 Ending
**Type**: ending
**Message**: 完整流程 + 关注引导
**Visual**: 简化流程图 + 作者信息
**Layout**: sparse
**Text**:
- 账号 → 支付 → 安装 → 配置 → 开干
- 有问题欢迎留言交流
- @老雷
