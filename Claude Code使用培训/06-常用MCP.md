# 第六阶段：常用 MCP 与集成

## 6.1 企业级 MCP

### mdold — 明道协作时代 MCP

mdold 对应明道协作时代 v1 API，是明道早期协作版本的接口。

**功能覆盖：**

| 功能 | 说明 |
|------|------|
| 任务管理 | 创建、查询、更新任务 |
| 日程管理 | 创建日历事件、邀请成员 |
| 消息 | 发送消息、获取聊天记录 |
| 组织 | 获取部门、成员通讯录 |
| 群组 | 群组管理、发帖 |

**配置方式：**

```bash
# 查看 mdold 相关 skill
ls ~/.agents/skills/ | grep mdold
```

**常用操作示例：**

```python
# 创建任务
mdold__task_add(
  task_name="完成设计方案",
  deadline="2026-04-15",
  charge_user_account_id="user123"
)

# 获取日程
mdold__calendar_get_events(
  start_date="2026-04-01",
  end_date="2026-04-30"
)

# 发送消息
mdold__webchat_send_message(
  message="会议将在5分钟后开始",
  group_id="group456"
)
```

---

### HAP MCP — 明道云 HAP MCP

HAP（Heybits Automation Platform）是明道云自己的零代码平台，适合搭建业务系统。HAP MCP 即 `mingdao` MCP。

**功能覆盖：**

| 功能 | 说明 |
|------|------|
| 工作表 | 创建表、字段、视图 |
| 记录 | 增删改查记录 |
| 自动化 | 触发工作流 |
| 统计图表 | 读取分析数据 |

**配置方式：**

```bash
# 使用 --scope user 全局安装
claude mcp add --scope user mingdao
```

---

## 6.2 邮箱 MCP

### Outlook MCP

通过 Microsoft Graph API 操作 Outlook 邮箱和日历。

**功能：**

| 功能 | 说明 |
|------|------|
| 读取邮件 | 列表、详情、搜索 |
| 发送邮件 | 支持附件、HTML 格式 |
| 日历 | 创建事件、查看日程 |
| 联系人 | 读取通讯录 |

**认证方式：**

```bash
# 使用 Microsoft 账号登录
ms365__login

# 发送邮件示例
ms365__send_mail(
  to=["recipient@example.com"],
  subject="会议邀请",
  body="明天下午3点开会"
)
```

### 网易邮箱 MCP

支持 163、126 等网易邮箱。

**功能：**

| 功能 | 说明 |
|------|------|
| 收取邮件 | IMAP 协议 |
| 发送邮件 | SMTP 协议 |
| 邮件搜索 | 关键词搜索 |

---

## 6.3 其他常用 MCP

### Google MCP — Gmail & Google Calendar

Claude.ai 官方提供两个独立的 Google MCP，分别接入 Gmail 和 Google Calendar。

**支持服务：**

| MCP | 服务 | 说明 |
|-----|------|------|
| claude.ai Gmail | Gmail | 搜索邮件、发送、标记星标、归档 |
| claude.ai Google Calendar | Google Calendar | 创建/修改/删除日程、查看日程列表 |

**配置：**

```bash
# 在 Claude.ai 账号设置中授权 Google 账号后自动连接
# 或使用 --scope user 添加：
claude mcp add --scope user "claude.ai Gmail"
claude mcp add --scope user "claude.ai Google Calendar"
```

### tencent-ad — 腾讯广告 API

管理腾讯广告投放。

**功能：**

| 功能 | 说明 |
|------|------|
| 广告账户 | 查询账户信息、日预算 |
| 广告组 | 创建、更新、出价 |
| 广告创意 | 上传素材、管理创意 |
| 数据报表 | 消耗、点击、转化数据 |

### ticktick — TickTick 任务管理

轻量级任务管理应用。

**功能：**

| 功能 | 说明 |
|------|------|
| 项目 | 创建项目、分类任务 |
| 任务 | 增删改查、设置优先级 |
| 标签 | 标签管理 |
| 子任务 | 任务拆解 |

**常用操作：**

```python
# 创建任务
ticktick__create_task(
  title="完成周报",
  due_date="2026-04-10",
  priority=3  # 0=无, 1=低, 3=中, 5=高
)

# 获取今日任务
ticktick__get_today_tasks()

# 获取高优先级任务
ticktick__get_high_priority_tasks(min_priority=3)
```

### 1password — 密码管理集成

安全地管理密码和密钥。

**功能：**

| 功能 | 说明 |
|------|------|
| 读取密码 | 从金库获取凭据 |
| 读取信用卡 | 安全卡片信息 |
| 读取 Secure Notes | 安全笔记 |

---

## MCP 选择建议

| 场景 | 推荐 MCP |
|------|---------|
| 明道协作时代（老版）| mdold |
| 明道云 HAP 低代码平台 | mingdao（HAP MCP）|
| 邮件（微软生态）| Outlook MCP |
| 邮件（国内）| 网易邮箱 MCP |
| Gmail | claude.ai Gmail |
| Google 日历 | claude.ai Google Calendar |
| 广告投放 | tencent-ad |
| 轻量任务 | ticktick |
| 密码管理 | 1password |
