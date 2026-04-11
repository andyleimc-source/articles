# Claude Code 培训课件大纲

> 讲师：Andy Lei
> 背景：讲师 Claude Code 使用时长超过 250 小时，本培训旨在帮助同事快速入门并掌握这一工具

---

## 课前必读

| 文档 | 路径 | 说明 |
|------|------|------|
| Claude Code 国内使用教程 | `articles/Claude Code国内使用` | 账号、翻墙、充值卡、海外验证码等前置准备 |

---

## 第一阶段：认识工具（0.5 小时）

### 1. Claude Code 是什么
- 官方 CLI 工具定位
- 与 ChatGPT、Web 版的核心差异
- 能做什么：写代码、读文件、执行命令、调用工具

### 2. Claude Code vs OpenClaw
- **Claude Code**：Anthropic 官方 CLI，纯命令行，专注本地开发
- **OpenClaw**：第三方 Agent 框架，支持微信/Telegram 接入，有心跳机制
- 各自适用场景
- 本培训的范围

---

## 第二阶段：环境准备（1 小时）

### 3. 必装环境

#### Core 工具链
```bash
# Homebrew - macOS 包管理器（必装第一步）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git - 版本控制
brew install git

# Node.js - npm 包管理器
brew install node

# Python - pip 包管理器
brew install pyenv
```

#### 常用软件安装
| 软件 | 安装方式 | 用途 |
|------|---------|------|
| VS Code | 官网下载 / brew | 代码编辑器 |
| iTerm2 | brew | 终端替代 |
| GitHub Desktop | 官网下载 | Git 图形化 |
| Termius | App Store / 官网 | 远程 SSH |

### 4. 翻墙与网络
- Shadowsocks 传统方案
- ClashVerge 现代代理管理
- 机场推荐与选购建议
- 配置示例

---

## 第三阶段：核心概念（2-3 小时）

### 5. CLI 基础和常用命令
- Claude Code 启动与退出
- 核心命令：`ask`、`exec`、`context`
- 命令行参数传递方式
- 输出解析方法

### 6. 目录管理与会话
- 工作目录（workspace）的概念
- 绝对路径 vs 相对路径
- Main Session vs Sub Session
- 会话持久化与上下文继承

### 7. 上下文管理系统
- System Prompt / SOUL.md / AGENTS.md
- Project Context 加载机制
- 长期记忆：MEMORY.md、daily notes
- HEARTBEAT 心跳机制

### 8. Skills 技能系统
- 什么是 Agent Skills
- 内置 Skills 列表与用途
- 如何使用一个 Skill
- 自定义 Skill 编写入门

### 9. MCP（Model Context Protocol）
- 什么是 MCP，为什么需要它
- 本机已安装 MCP 一览
- MCP 如何与 Skills 协同

---

## 第四阶段：权限与安全（0.5 小时）

### 10. Claude Code 权限开通
- bypass permission on 模式
  - 适用场景
  - 风险提示（⚠️ 谨慎使用）
- 系统权限配置
  - 屏幕录制权限
  - 控制电脑权限（Accessibility）
  - 在系统偏好设置中操作路径

---

## 第五阶段：开发工具链（1.5 小时）

### 11. Git 与 GitHub
- Git 基础概念（仓库、提交、分支）
- GitHub 账号注册与 SSH 密钥配置
- 常用 Git 命令速查
- GitHub Desktop 使用
- Pull Request 流程简介

### 12. 前端三剑客（入门）
> 💡 说明：此处仅作概念扫盲，不做深度开发教学

#### HTML - 网页结构
- 标签、元素、属性的概念
- 常用标签一览

#### CSS - 网页样式
- 选择器、盒模型
- Flexbox 布局入门

#### JavaScript - 网页交互
- 变量与数据类型
- DOM 操作概念
- 事件处理入门

### 13. 语言安装库的概念
- 以 Python/pip 为例讲解原理
- Node.js / Go / Ruby 包管理器对比
- 虚拟环境的概念

### 14. 前后端概念扫盲
- 前端：界面、交互
- 后端：API、数据、业务逻辑
- 全栈协作模式
- Claude Code 如何辅助前后端开发

---

## 第六阶段：常用 MCP 与集成（1.5 小时）

### 15. 企业级 MCP
| MCP 名称 | 功能 | 场景 |
|---------|------|------|
| mdold | 明道云 API | 任务、日历、消息 |
| HAP MCP | 维格表 API | 表、视图、自动化 |
| Outlook MCP | 邮件、日历 | 邮件管理 |
| 网易邮箱 MCP | 邮箱 | 邮件收发 |

### 16. 其他常用 MCP
- `gog`：Google Workspace（Gmail, Calendar, Drive）
- `tencent-ad`：腾讯广告 API
- `ticktick`：TickTick 任务管理
- `1password`：密码管理集成

---

## 第七阶段：特殊插件（0.5 小时）

### 17. Claude use Chrome
- Chrome CDP 协议连接
- 控制浏览器的场景
- 使用示例演示

### 18. Claude use Desktop
- macOS 桌面自动化
- 系统级操作能力
- 安全注意事项

---

## 第八阶段：远程使用（1 小时）

### 19. 远程使用 Claude Code

#### Tailscale 内网穿透
- 安装与设备组网
- 获取设备节点 IP
- 安全机制说明

#### Termius 远程终端
- SSH 连接配置
- 密钥管理
- 会话持久化

#### 完整流程
```
本地 → Tailscale 组网 → 服务器 IP → Termius SSH → 远程 Claude Code
```

---

## 第九阶段：附属知识（可自学）

### 20. 海外账号体系

| 平台 | 说明 | 注册要点 |
|------|------|---------|
| Gmail | 美区 Google 账号 | 海外手机号验证 |
| GitHub | 代码平台 | 已覆盖在第三章 |
| 美区 Apple ID | App Store 海外应用 | 独立账号体系 |

### 21. 美区账号注册进阶
- 虚拟海外手机号获取
- 充值卡购买渠道
- 验证码收取平台
- 注意事项与避坑指南

> 📖 详细教程见：`articles/Claude Code国内使用`

---

## 附录

### 课件文件清单

```
articles/Claude Code使用培训/
├── Claude Code 培训课件大纲.md          ← 完整大纲
├── 01-认识工具.md
├── 02-环境准备.md
├── 03-核心概念.md
├── 04-权限与安全.md
├── 05-开发工具链.md
├── 06-常用MCP.md
├── 07-特殊插件.md
├── 08-远程使用.md
├── 09-附属知识.md
├── 10-Claude Code vs OpenClaw.md
├── 练习手册.md                        ← 理论题 + 实操任务 + 挑战题
└── Claude Code培训-乔布斯风PPT.html   ← 16页竖屏演示稿（可直接浏览器打开）
```

### 课程资源索引
| 资源 | 路径 |
|------|------|
| 培训课件（正文）| `articles/Claude Code使用培训/` |
| PPT 演示稿 | `Claude Code培训-乔布斯风PPT.html`（浏览器直接打开）|
| 练习手册 | `练习手册.md` |
| 国内使用教程 | `articles/Claude Code国内使用/` |
| OpenClaw 文档 | https://docs.openclaw.ai |
| Claude Code CLI | Anthropic 官方 |

---

## 建议课时安排

| 阶段 | 内容 | 时长 | 教学方式 |
|------|------|------|---------|
| 课前 | 安装 Claude Code、注册 GitHub | - | 自学 |
| 第一阶段 | 认识工具 | 0.5h | 讲解 |
| 第二阶段 | 环境准备 | 1h | 实操 |
| 第三阶段 | 核心概念 | 2-3h | 讲解 + 演示 |
| 第四阶段 | 权限与安全 | 0.5h | 实操 |
| 第五阶段 | 开发工具链 | 1.5h | 讲解 + 练习 |
| 第六阶段 | 常用 MCP | 1.5h | 演示 |
| 第七阶段 | 特殊插件 | 0.5h | 演示 |
| 第八阶段 | 远程使用 | 1h | 实操 |
| 第九阶段 | 附属知识 | - | 自学 |

**总建议时长：约 9-10 小时（可分 4-5 次课）**

### 配套材料

| 材料 | 说明 | 何时使用 |
|------|------|---------|
| **乔布斯风 PPT** | 16 页竖屏演示，浏览器打开即可 | 课堂讲解投影 / 学员预习 |
| **练习手册** | 每阶段配理论题 + 实操任务 + 挑战题 | 课后作业 / 课堂实操 |
| **详细课件正文** | 10 个章节的完整内容 | 深入学习 / 讲师备课 |

---

## 课件文件清单

```
articles/Claude Code使用培训/
├── Claude Code 培训课件大纲.md   ← 本文件
├── 01-认识工具.md
├── 02-环境准备.md
├── 03-核心概念.md
├── 04-权限与安全.md
├── 05-开发工具链.md
├── 06-常用MCP.md
├── 07-特殊插件.md
├── 08-远程使用.md
├── 09-附属知识.md
└── （练习素材）
```

---

*Last Updated: 2026-04-06*
