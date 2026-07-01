# 小红书 11 张卡片 outline

文章：cc-token-waste-10 / 真正烧 Claude Code token 的 10 个习惯
策略：B 信息密集型 · 风格：notion · 配色：雷码工坊磷绿 v2 · 比例：3:4 · 后端：seedream 5.0
水印：右下角「雷码工坊笔记」石墨色 65%
锚点：image 1 (cover) 不带 ref，01-10 全部 --ref cover

## 卡片清单

| # | 文件名 | 类型 | 主标题 | 钩子 | 主视觉 |
|---|---|---|---|---|---|
| 00 | 00-cover.png | cover/sparse | 真正烧 token 的 10 个习惯 | superpowers 不在里面 | 燃烧的 token 计量表，磷绿火苗 |
| 01 | 01-clear.png | content/balanced | 该 /clear 不 clear | 换任务就 /clear | 堆叠的对话气泡像砖墙压顶 |
| 02 | 02-mcp.png | content/balanced | 装一堆用不上的 MCP | 8 个工具全程陪跑 | 会议桌坐 8 个不说话的同事 |
| 03 | 03-skill.png | content/balanced | 全局塞用不到的 skill | 每周用一次吗 | 工具墙落灰 |
| 04 | 04-claudemd.png | content/balanced | CLAUDE.md 写成长篇 | 每轮朗读 50 遍 | 长卷轴重复展开 |
| 05 | 05-find-file.png | content/balanced | 让它自己找文件 | 直接 @path | 迷宫 vs 直线 |
| 06 | 06-subagent.png | content/balanced | 大任务不用 subagent | 让子代理读 | 主屋 vs 隔壁工作间 |
| 07 | 07-cat.png | content/balanced | 用 cat 读大文件 | Read 加 offset/limit | 整本书 vs 单页 |
| 08 | 08-rollback.png | content/balanced | 改错了不回退 | git checkout 回干净 | 歪楼积木 vs 推倒重来 |
| 09 | 09-plan.png | content/balanced | 不用 plan mode 直接干 | 看计划省 70% | 地图 vs 蒙眼狂奔 |
| 10 | 10-repeat.png | content/balanced | 重复贴代码报错 | 让它 Read 当前版本 | 复印机吐重复纸 |

## 文字稳定区
- 单行 ≤10 汉字
- 整图 ≤40 字
- prompt 显式约束字形正确，无错字

## 通用 prompt 片段
- Style: Notion-style flat illustration, hand-drawn slightly imperfect outlines, warm editorial feel, paper-grain texture, plenty of negative space
- Palette: background ink-cream #FAF7F0; main outlines / titles ink-black #0E1116 (NEVER pure black); accent / signal / CTA phosphor-green #1AB87C; subtitle / labels graphite #3A4151; secondary fog-blue #9CB4CC; shadows brick-grey #6E6259
- FORBID: purple gradient, neon, cyberpunk, teal/cyan, orange/coral, photorealistic, 3D cartoon
- Text constraint: Chinese glyphs must render correctly, no garbled characters, no fake-looking CJK, kerning correct, single-line ≤10 Chinese characters
- Watermark: small "雷码工坊笔记" at bottom-right corner, graphite color #3A4151, ~65% opacity, sans-serif, no icon no border
