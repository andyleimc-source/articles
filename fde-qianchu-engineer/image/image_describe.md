# 配图说明

## 真实页面截图（Chrome DevTools MCP 抓取）

| 文件 | 来源 | 在文章里的论点支撑 | 抓取时间 |
|---|---|---|---|
| `01-openai-deployco.png` | https://openai.com/index/openai-launches-the-deployment-company/ | 开篇钩子：OpenAI DeployCo 官宣页副标题写明 "Forward Deployed Engineers from day one" | 2026-05-17 |
| `02-anthropic-fde-jd.png` | https://job-boards.greenhouse.io/anthropic/jobs/4985877008 | 第 1 节：Anthropic 实际招聘 FDE 的硬证据，6 城市同时开 | 2026-05-17 |
| `04-levelsfyi-palantir-fdse.png` | https://www.levels.fyi/companies/palantir/salaries/software-engineer/title/fdse | 第 6 节：Palantir FDSE 真实薪资数据（中位 $215K、顶部 $415K+），同时反向证明「前沿部署」译名已污染主流数据平台 | 2026-05-17 |
| `05-levie-tweet-fde.png` | https://x.com/levie/status/2044225408972009842 | 第 1 节：Aaron Levie 2026-04-15 长推截图，17 万阅读 | 2026-05-17 |

抓取方式：Chrome DevTools MCP，1400×900 视口，sips 裁剪 + 缩到 1200px 长边（WeChat 兼容）。

## Notion 风手绘插图（baoyu-imagine + Seedream 5.0 生成）

| 文件 | 位置 | 内容 | 作用 |
|---|---|---|---|
| `06-translation-grid.jpg` | 第二节末尾 | 6 个译名卡片：5 个错译（✗）+ 1 个推荐译名「前出工程师」（✓ 绿色高亮） | 把第二节最硬核的译名诊断视觉化，方便读者收藏后回查 |
| `07-timeline.jpg` | 第三节末尾 | 横向时间轴：2008 Palantir / 2020 PoC 撞墙 / 2024 五家集体开岗 / 2025 Levie 推文 / 2026 OpenAI DeployCo | 把事件密集的 FDE 简史变成视觉锚点，提升记忆效率 |
| `08-decision-tree.jpg` | 第四节开头 | 三档客单价 → 三种决策的分流图，中间档磷绿高亮 | 给 SaaS 老板一眼看完的决策树，比表格更直觉 |
| `09-career-paths.jpg` | 第六节开头 | 四类身份（学生 / 研发 / 售前 / PM）→ 四条不同长度的路径汇聚到「前出工程师」徽章 | 把第六节最长的转型指南视觉化，减缓阅读疲劳 |

生成方式：4 个 prompt 文件存档在 `../prompts/06-09-*.md`，统一 Notion 编辑器手绘风 + 雷码工坊品牌色 v2（米白底/墨黑线/磷绿强调/雾蓝/砖灰）+ 右下角「雷码工坊笔记」水印 + 16:9 横版。

注：原计划用 gpt-image-2，本地 TLS 证书校验失败，回退到 Seedream 5.0（也确保跟 cover.png 视觉风格统一）。
