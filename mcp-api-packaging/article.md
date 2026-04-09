# 我用 Claude Code，把任何 API 文档变成了 AI 可以直接调用的工具

上周我做了一件事，做完之后自己愣了一下。

我把腾讯广告的整个 API，358 个接口，全部变成了 Claude 可以直接调用的工具。整个过程，我没有写一行核心代码——Claude Code 写的。我只是喂了文档，盯着它干活，偶尔纠正方向。

做完之后我在想：这件事以前需要多少时间？

一个靠谱的后端工程师，仔细读完 358 个接口的文档、写完所有封装代码、调试签名逻辑、处理错误返回——保守估计两周。现在，半天。

我不是在夸 Claude，我是真的被这个速度吓到了。

---

## MCP 是什么，为什么你应该关心

在说具体怎么做之前，先解释一个概念：**MCP（Model Context Protocol）**。

这是 Anthropic 在 2024 年推出的开放标准，解决了一个很实际的问题：AI 助手怎么跟外部系统连接？

以前的答案是"写插件"、"做 function calling"，每家 AI 都有自己的格式，对接一次就是一个项目。MCP 的出现，相当于给 AI 的外部连接定了一个标准接口——类似 USB 之于硬件。

一旦你把一个 API 封装成 MCP 服务，**所有支持 MCP 的 AI 客户端都能直接用**：Claude Desktop、Cursor、Windsurf、以及未来更多工具。

这意味着什么？

你可以在 Claude 里直接说："帮我查一下这个广告账户昨天的消耗，和上周同期对比一下。"Claude 会自动调用腾讯广告 API，拿到数据，帮你分析，给你结论。你不需要打开任何广告后台，不需要导出任何表格。

这不是演示，这是我今天实际在用的东西。

---

## 两个真实案例

在我讲方法之前，先讲两个我做出来的东西。

### 案例一：即梦 AI MCP（jimeng-ai-mcp）

即梦是字节跳动旗下的 AI 图片/视频生成平台，有官方的 Volcengine API。

我把它封装成了 MCP 服务，里面有 9 个工具：

- `generate_image`：文字生成图片，支持即梦 4.0、4.6 等多个模型
- `image_to_image`：参考图改图
- `inpaint_image`：局部重绘，涂掉哪里改哪里
- `upscale_image`：低清图放大到 4K/8K
- `generate_video`：文字生成视频
- `image_to_video`：图片变视频，支持首尾帧驱动
- `imitate_motion`：动作模仿，把参考视频的动作迁移到目标人物
- `generate_digital_human`：图片 + 音频，生成口型同步的数字人视频
- `translate_video`：视频翻译，保留原始音色，口型同步换语言

现在我在 Claude 里生成图片，就是一句话的事："帮我生成一张宋代山水画风格的图，16:9，用即梦 4.0 模型"。Claude 直接出图，保存到本地。

**GitHub：** https://github.com/andyleimc-source/jimeng-ai-mcp
**安装：** `pip install jimeng-ai-mcp`（或 `uvx jimeng-ai-mcp`）

### 案例二：腾讯广告 MCP（tencent-ad-mcp）

这个工程量更大。腾讯广告的营销 API 3.0 有 358 个接口，覆盖广告账户、投放、素材、报表、受众……几乎所有操作。

我同样把它封装成了 MCP，现在这 358 个工具都在 Claude 里待命。

**GitHub：** https://github.com/andyleimc-source/tencent-ad-mcp

---

## 原理：Claude Code 在这里做了什么

传统的 API 封装，本质上是体力活：读文档、写函数、处理参数、对齐格式、调试签名、写错误处理……每个接口都要重复一遍，枯燥且耗时。

Claude Code 的优势，恰好在这里。它能：

1. **批量理解文档**：把整份 API 文档喂给它，它能理解每个接口的参数、返回值、必填项、枚举值
2. **生成规范代码**：按照你定义的代码结构，一次性生成所有工具的封装
3. **处理边界情况**：签名算法、错误码映射、异步轮询……这些烦人的细节它能处理
4. **自我纠错**：遇到报错，给它看错误日志，它能定位问题重写

整个流程的本质是：**你负责定方向和审核，Claude Code 负责执行**。

---

## 完整步骤：从 API 文档到可安装的工具包

下面是我实际走过的流程，你照着做就能复制。

### 第一步：准备 API 文档

找到你要封装的 API 的官方文档。越完整越好，至少要包含：
- 接口地址和请求方式
- 必填/选填参数及类型
- 返回值结构
- 鉴权方式（API Key、HMAC 签名等）

把文档保存成本地文件，或者告诉 Claude Code 文档的 URL。

### 第二步：建立项目结构

用 Claude Code 创建一个标准的 MCP 项目结构。Python 项目通常是：

```
your-api-mcp/
├── src/
│   └── your_api_mcp/
│       ├── server.py    # MCP 工具定义
│       ├── client.py    # API 调用逻辑
│       ├── auth.py      # 鉴权
│       └── models.py    # 常量/模型标识符
├── pyproject.toml       # 包配置
├── .env.example
└── README.md
```

告诉 Claude Code："用 Python + MCP SDK 创建一个项目骨架，用于封装 [你的 API 名称]"。

### 第三步：实现鉴权

这是最容易出错的地方。把 API 文档里的鉴权章节完整给 Claude Code，让它实现。

对于复杂签名（比如 Volcengine 的 HMAC-SHA256 签名），可以说："照这个签名规范实现一个 build_signed_request 函数"，然后用官方提供的示例请求验证正确性。

### 第四步：批量生成工具

这是关键步骤，也是最省时间的地方。

把所有接口的文档（或者按模块分批）给 Claude Code，说："按这个格式，为每个接口生成一个 MCP 工具函数"，然后给它看一个已经写好的示例工具。

Claude Code 会按照你的模式，批量生成剩余所有接口的封装代码。

**腾讯广告那个项目，358 个接口就是这样批量生成的。**

### 第五步：发布到 GitHub

```bash
git init
git add .
git commit -m "Initial release"
gh repo create your-api-mcp --public --push
```

### 第六步：发布到 PyPI（Python 项目）

在 `pyproject.toml` 里配置好包名、版本、依赖，然后：

```bash
uv build
uv publish
```

第一次发布需要 PyPI 账号和 token。发布成功后，别人就可以直接 `pip install your-api-mcp` 或 `uvx your-api-mcp` 使用。

**设置 GitHub Actions 自动发布（推荐）：**

创建 `.github/workflows/publish.yml`，配合 PyPI 的 Trusted Publisher，每次打 tag 自动发布：

```yaml
name: Publish to PyPI
on:
  push:
    tags:
      - "v*"
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv build
      - uses: pypa/gh-action-pypi-publish@release/v1
```

配置好之后，发新版本只需要两行：

```bash
git tag v0.2.0
git push origin v0.2.0
```

---

## 别人怎么用你做的 MCP 工具

以即梦 MCP 为例，安装和配置只需要 5 分钟：

**1. 获取密钥**

去火山引擎控制台开通对应服务，拿到 Access Key ID 和 Secret Access Key。

**2. 配置 Claude Desktop**

打开配置文件（macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`，Windows: `%APPDATA%\Claude\claude_desktop_config.json`），加入：

```json
{
  "mcpServers": {
    "jimeng": {
      "command": "uvx",
      "args": ["jimeng-ai-mcp"],
      "env": {
        "JIMENG_ACCESS_KEY_ID": "你的密钥",
        "JIMENG_SECRET_ACCESS_KEY": "你的密钥"
      }
    }
  }
}
```

**3. 重启 Claude Desktop，直接对话**

> "帮我生成一段 10 秒的视频：一只狐狸在雪地里奔跑，慢镜头，电影感"

Claude 自动调用接口，生成完保存到本地，对话里展示结果。

---

## 这件事更大的意义

说实话，我做这两个项目的时候，并没有太把它当回事。就是觉得"这个 API 能用，封装一下让 Claude 能调用挺好的"。

但做完之后仔细想，这个模式本身值得认真对待。

**任何有 API 的服务，都可以这样变成 AI 可以直接操作的工具。**

不是一个，是所有。ERP、CRM、广告平台、电商后台、数据仓库、内部系统……只要有文档，只要有鉴权，用 Claude Code，半天到一天就能封装出来。

以前我们讲"AI 辅助工作"，大多数时候是 AI 帮你写写文档、改改代码、总结总结会议纪要。有用，但本质上还是人在操作系统，AI 在旁边递工具。

MCP 改变了这个结构。**AI 开始直接操作系统，人退到指挥层。**

你说指令，AI 查数据、跑接口、生成内容、整合结果——整个执行链路，AI 在里面跑。

这不是未来。这是我今天用的工作方式。

> 任何还没有被 MCP 接入的 API，都是一个等待被解锁的超能力。

---

**关于作者**

<img src="image/author_avatar_andy.png" height="200">

**老雷（Andy）**，明道云 & Nocoly CMO，SaaS 行业从业十余年。骨子里是个产品人和技术迷，乔布斯的信徒，相信好的产品能改变世界。深度关注 AI、商业与科技趋势，目前在深度使用和实践 Claude Code，专注探索 AI 如何重塑产品形态和商业逻辑。不聊概念，只聊真实发生的事。
