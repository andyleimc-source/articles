# AI 就业·盯盘人 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 写一篇约 5000 字的中文文章《盯盘人》，配 8 张插图，同步生成英文版、小红书组图、推广文案，最终发布到微信公众号和小红书。

**Architecture:** 先建目录结构 → 逐节写中文正文 → 生成/收集配图 → 写英文版 → 生成小红书组图 → 写推广文案 → 审核 → 发布。

**Tech Stack:** Markdown、baoyu-danger-gemini-web（配图生成）、baoyu-cover-image（封面）、baoyu-xhs-images（小红书）、baoyu-article-illustrator（插图分析）、baoyu-post-to-wechat（发布）、WebSearch（历史图片）

---

## 文件结构

```
/Users/andy/Documents/articles/ai-employment-panman/
├── article.md               # 中文正文（主文件）
├── article-en.md            # 英文版
├── cover.png                # 封面图 2.35:1（由 cover.svg 导出）
├── promotion.md             # 推广文案（仅本地，不推送）
├── image_describe.md        # 图片说明文档
└── image/
    ├── cover.png            # 封面图
    ├── 01-panman.webp       # baoyu生成：盯盘人概念图
    ├── 02-industrial.jpg    # 网络：工业革命工厂
    ├── 03-office-1990s.jpg  # 网络：1990s办公室
    ├── 04-ai-wave.webp      # baoyu生成：AI浪潮示意
    ├── 05-busier.webp       # baoyu生成：工具升级→更忙时间轴
    ├── 06-jobs.jpg          # 网络：乔布斯照片
    ├── 07-tool-matrix.webp  # baoyu生成：工具选择矩阵
    ├── 08-pioneer.webp      # baoyu生成：浪头开拓者
    └── author_avatar_andy.png
```

---

## Task 1: 建立目录结构

**Files:**
- Create: `/Users/andy/Documents/articles/ai-employment-panman/`（目录）
- Create: `/Users/andy/Documents/articles/ai-employment-panman/image/`（目录）

- [ ] **Step 1: 建目录**

```bash
mkdir -p /Users/andy/Documents/articles/ai-employment-panman/image
```

- [ ] **Step 2: 复制作者头像**

```bash
cp /Users/andy/Documents/articles/steve-jobs-interface/image/author_avatar_andy.png \
   /Users/andy/Documents/articles/ai-employment-panman/image/
```

- [ ] **Step 3: 验证**

```bash
ls /Users/andy/Documents/articles/ai-employment-panman/image/
```
Expected: `author_avatar_andy.png`

- [ ] **Step 4: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/
git commit -m "init: create ai-employment-panman article directory"
```

---

## Task 2: 生成封面图（2.35:1）

**Files:**
- Create: `ai-employment-panman/image/cover.png`

- [ ] **Step 1: 调用 baoyu-cover-image skill**

使用 `baoyu-skills:baoyu-cover-image` skill，参数：
- 文章标题：《盯盘人》
- 副标题：当 AI 能完成大部分执行，人的价值往哪里放？
- 风格：notion 手绘，极简，黑白灰为主
- 比例：2.35:1（宽 1280px × 高 544px）
- 核心视觉元素：一个人坐在屏幕前俯瞰自动运转的流程，周围漂浮着数据和任务卡片

- [ ] **Step 2: 保存封面图**

生成后保存到 `ai-employment-panman/image/cover.png`，同时在文章目录根目录放一份 `cover.png`。

- [ ] **Step 3: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/cover.png ai-employment-panman/image/cover.png
git commit -m "add: cover image for 盯盘人"
```

---

## Task 3: 生成 baoyu 概念配图（4张）

**Files:**
- Create: `ai-employment-panman/image/01-panman.webp`
- Create: `ai-employment-panman/image/05-busier.webp`
- Create: `ai-employment-panman/image/07-tool-matrix.webp`
- Create: `ai-employment-panman/image/08-pioneer.webp`

使用 `baoyu-skills:baoyu-danger-gemini-web` skill（Gemini 结构，notion 手绘风）。

- [ ] **Step 1: 生成图 01-panman（盯盘人）**

Prompt（英文，Gemini 效果更好）：
```
Notion-style hand-drawn illustration. A person sits at a desk staring at a large monitor. 
On the screen: multiple automated workflow cards floating around, arrows connecting tasks, 
checkboxes auto-completing themselves. The person looks calm, just watching, not doing. 
Minimal line art, black and white with light gray shading. Clean, editorial feel.
No text in image.
```
保存为 `image/01-panman.webp`

- [ ] **Step 2: 生成图 05-busier（工具升级→更忙时间轴）**

Prompt：
```
Notion-style hand-drawn horizontal timeline illustration.
4 eras left to right: Agricultural Age (person with hoe, relaxed), Industrial Age (factory worker, busy), 
Internet Age (office worker at PC, very busy), AI Age (person at laptop surrounded by AI tools, extremely busy).
Above each era: a small bar chart showing productivity going up, and work hours also going up.
Simple line art, minimal, black and white. No text labels needed.
```
保存为 `image/05-busier.webp`

- [ ] **Step 3: 生成图 07-tool-matrix（工具选择矩阵）**

Prompt：
```
Notion-style hand-drawn 2x2 matrix diagram.
X-axis label area: "Price" (left=Low, right=High).
Y-axis label area: "Capability" (bottom=Low, top=High).
Top-left quadrant: a simple robot icon labeled "MiniMax" with a small coin icon (low price, decent capability).
Top-right quadrant: a powerful robot icon labeled "Claude Code" with a crown (high price, highest capability).
Bottom areas: empty/crossed out.
Clean hand-drawn style, black ink on white, minimal shading.
```
保存为 `image/07-tool-matrix.webp`

- [ ] **Step 4: 生成图 08-pioneer（浪头开拓者）**

Prompt：
```
Notion-style hand-drawn illustration. A small human figure stands confidently on top of a giant wave.
The wave is made of flowing data streams, code snippets, and circuit patterns.
The person looks forward into an open horizon with a sunrise. 
Behind: dark storm clouds (old ways). Ahead: bright open sky.
Dramatic but minimal. Black and white with one accent of light gray wash on the wave.
No text.
```
保存为 `image/08-pioneer.webp`

- [ ] **Step 5: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/image/01-panman.webp \
        ai-employment-panman/image/05-busier.webp \
        ai-employment-panman/image/07-tool-matrix.webp \
        ai-employment-panman/image/08-pioneer.webp
git commit -m "add: baoyu generated concept illustrations"
```

---

## Task 4: 收集网络历史配图（4张）

**Files:**
- Create: `ai-employment-panman/image/02-industrial.jpg`
- Create: `ai-employment-panman/image/03-office-1990s.jpg`
- Create: `ai-employment-panman/image/04-ai-wave.jpg`
- Create: `ai-employment-panman/image/06-jobs.jpg`

使用 `WebSearch` 工具搜索，用 `mcp__claude-in-chrome__*` 工具下载。

- [ ] **Step 1: 搜索工业革命图片**

Search query: `industrial revolution factory interior 1800s workers machines historical photo`
目标：寻找有工人和机器、画面感强的工厂内景黑白照片或版画。
保存最合适的一张为 `image/02-industrial.jpg`

- [ ] **Step 2: 搜索 1990s 办公室图片**

Search query: `1990s office workers computers cubicles vintage photo`
目标：一排员工坐在电脑/打字机前的典型90年代办公室场景。
保存为 `image/03-office-1990s.jpg`

- [ ] **Step 3: 搜索 AI 浪潮/裁员相关图片**

Search query: `artificial intelligence automation jobs disruption illustration`
目标：AI 替代人工的概念示意图，或大厂裁员相关新闻配图风格。
保存为 `image/04-ai-wave.jpg`

- [ ] **Step 4: 搜索乔布斯照片**

Search query: `Steve Jobs Apple keynote product design thinking photo`
目标：乔布斯经典演讲或产品思考照片，有质感。
保存为 `image/06-jobs.jpg`

- [ ] **Step 5: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/image/02-industrial.jpg \
        ai-employment-panman/image/03-office-1990s.jpg \
        ai-employment-panman/image/04-ai-wave.jpg \
        ai-employment-panman/image/06-jobs.jpg
git commit -m "add: historical and reference images"
```

---

## Task 5: 写中文正文 article.md（第一、二节）

**Files:**
- Create: `ai-employment-panman/article.md`

- [ ] **Step 1: 创建文件，写文章头部 + 第一节（盯盘人诞生）**

写入以下内容（开头标签 + 第一节完整正文，约 600 字）：

```markdown
<img src="cover.png">

# 盯盘人

> 当 AI 能完成大部分执行，人的价值往哪里放？

---

### 一、盯盘人诞生

[开篇场景：同事小X第一次用 Claude Code 的震撼时刻]

核心内容要点（写作时展开成叙事，约600字）：
- 场景还原：老雷教他学会 Claude Code
- 他之前的工作：一个个催销售补客户信息，容易忘，不知道什么时候该跟进，大量复制粘贴
- Claude Code 之后：系统自动补全信息、自动分析哪条优先、自动规划跟进时间——他只需要"盯盘"
- 画面感：他坐在屏幕前，看着任务卡片一张张自动完成
- 他的问题：以后人都不需要工作了，人去干啥？
- 老雷的回答：你就拥抱它就行了
- 他的表情：既诧异又困惑，想不明白
- 打住——悬念留给结尾

<img src="image/01-panman.webp" height="300">
*当 AI 接管执行，你只需要盯盘*

---
```

- [ ] **Step 2: 写第二节（历史：人类一直在升维）**

追加到 article.md，约 800 字：

核心内容要点：
- 农业时代 → 工业时代：纺织工被机器取代，工厂监工/铁路调度/流水线管理员大量出现
- 有画面感的具体场景：曼彻斯特的工厂、蒸汽机的轰鸣、狄更斯笔下的工人进城
- 关键转折：这批人没有消失，他们进化成了穿西装坐在办公室里的"文员监管者"
- 关键洞察：工业化之前没有"八小时工作制"，人看似清闲，但物质极度匮乏；工业化之后人反而更忙，但财富开始积累
- 八小时工作制是工业化之后才出现的——为了保护过度劳动的工人
- 这不是偶然：每当生产工具升级，人类的工作强度都会短暂上升，然后财富跟着上升

```markdown
### 二、人类一直在"升维"

<img src="image/02-industrial.webp" height="300">
*曼彻斯特的纺纱厂，1835年——那批纺织工人并没有消失，他们变成了监工*

[正文 800 字]

---
```

- [ ] **Step 3: 验证文件**

```bash
wc -w /Users/andy/Documents/articles/ai-employment-panman/article.md
```
Expected: 约 400-600 words (中文字数约 700-900)

- [ ] **Step 4: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/article.md
git commit -m "wip: article sections 1-2"
```

---

## Task 6: 写中文正文（第三、四节）

**Files:**
- Modify: `ai-employment-panman/article.md`

- [ ] **Step 1: 追加第三节（互联网时代重演）**

约 600 字，核心内容：
- 打字员消失 → 程序员崛起
- 广告公司裁了手绘美工 → 来了会 PS 的数字设计师
- SaaS 干掉了一批 IT 运维 → 带来了 CS/客户成功岗位
- 每次都有人哭，每次都有新工种；但门票换了
- Excel 类比提前埋线：早期会用 Excel 的人是核心竞争力（后文回收）

```markdown
### 三、互联网时代重演了一遍

<img src="image/03-office-1990s.webp" height="300">
*1990年代的办公室：打字员正在消失，但键盘还没有*

[正文 600 字]

---
```

- [ ] **Step 2: 追加第四节（这次不一样的地方）**

约 700 字，核心内容：
- 前两次替代的是体力和重复脑力；这次 AI 直冲"创意执行"
- 具体列举：写文案、写代码、做设计、做数据分析——这些曾经被认为是"人类专属"的工作
- 海外案例（需要写实数据，用 WebSearch 查最新数据）：Meta 2024-2025 裁员、Klarna 用 AI 替代 700 名客服、黑石削减分析师岗位
- 国内为什么还没炸：两个原因——①领导自己用得不好，不清楚威力；②体制对裁员谨慎
- 但不是不来，是还没来——一旦某家大厂带头，多米诺就倒
- 紧迫感：AI 进化按周计算，窗口在快速关闭

```markdown
### 四、这次，不是重演，是加速

<img src="image/04-ai-wave.webp" height="300">
*Klarna 用 AI 替代了 700 名客服——这不是新闻，这是预告*

[正文 700 字]

---
```

**注意**：写第四节前，先用 WebSearch 查以下数据：
- Klarna AI replaces customer service jobs 2024 数量
- Meta layoffs AI 2024-2025
- 其他大厂用AI裁员的具体案例和数字

- [ ] **Step 3: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/article.md
git commit -m "wip: article sections 3-4"
```

---

## Task 7: 写中文正文（第五、六节）

**Files:**
- Modify: `ai-employment-panman/article.md`

- [ ] **Step 1: 追加第五节（反直觉：AI 来了更忙了）**

约 500 字，核心内容：
- 老雷个人感受：AI 工具用起来之后，反而停不下来，工作量更大了
- 原理：门槛降了 → 能做的事变多了 → 你开始做以前"想做但没能力做"的事
- 历史印证：工业化之前农民"日出而作日入而息"看似清闲，但其实产出极低；工业化之后每周工作 60-80 小时，但物质财富爆炸
- AI 时代的产品爆炸：个性化、定制化的产品和内容会极其丰富，创作者的产能飙升
- 这不是负担，是机会——对那些真的在用 AI 的人

```markdown
### 五、AI 来了，我反而更忙了

<img src="image/05-busier.webp" height="300">
*每次生产工具升级，人类都变得更忙——但也更富*

[正文 500 字]

---
```

- [ ] **Step 2: 追加第六节（品位与判断力）**

约 700 字，核心内容（文章思想密度最高的节）：
- 当执行成本趋近于零，稀缺的是什么
- 乔布斯那句话的背景：1996 年采访，他说微软没有品位（"They have no taste"）——不是技术不行，是不知道什么是好东西
- AI 不会告诉你"应该做什么"——这由你的价值观决定
- AI 不会告诉你"做成什么样才是好的"——这由你的品位决定
- AI 让每个人都能生产，但品位高的人做出来的东西依然不同凡响
- 品位的构成：①对世界的理解——哲学、历史、文化的沉淀，这些决定你的视角；②个人成长经历——每个阶段塑造独特的感受力
- 怎么练品位：广泛阅读经典（不是当装饰，是作为原材料）、看优秀作品并做理性分析
- 品位是可以练出来的，但需要时间和主动投入——这恰恰是 AI 给不了你的东西

```markdown
### 六、盯盘人，盯的是什么

<img src="image/06-jobs.webp" height="300">
*"他们没有品位。" — 史蒂夫·乔布斯，1996*

[正文 700 字]

---
```

- [ ] **Step 3: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/article.md
git commit -m "wip: article sections 5-6"
```

---

## Task 8: 写中文正文（第七、八节 + 作者介绍）

**Files:**
- Modify: `ai-employment-panman/article.md`

- [ ] **Step 1: 追加第七节（实操：工具层面怎么做）**

约 500 字，核心内容：
- 回收第三节的 Excel 埋线：早期会用 Excel = 核心竞争力，现在人人会用 = 水平拉平。AI 的深度比 Excel 深得多
- 不建议把所有 AI 工具都学一遍，策略：
  - 最便宜的：MiniMax——国产、订阅型、日常高频使用不担心账单
  - 最强的：Claude Code——处理复杂任务、最强推理能力、最佳体验
  - 掌握这两个，既不用担心账单，也能处理最难的工作
- 关键：不是简单"用"，是用 AI 做执行，把自己的精力全部投入"判断"和"提升品位"
- 如果只把 AI 当简单工具，水平很快被拉平；如果用它撬动更高阶的能力，天花板完全不同

```markdown
### 七、工具层面，怎么用

<img src="image/07-tool-matrix.webp" height="300">
*选工具的逻辑：一个最便宜，一个最强*

[正文 500 字]

---
```

- [ ] **Step 2: 追加第八节（收束）**

约 600 字，核心内容：
- 回收开篇：同事那个诧异困惑的表情
- 他当时在问错误的问题："我的哪些工作会消失？"
- 应该问的问题："我能用它创造什么？"
- 我们是第一批站在浪头的人——中国在 AI 技术上并没有落后太多（Claude Code 等最强功能也是最近半年才出现的）
- 这是一场真实的革命，意义不亚于互联网的发明；未来几十年都围绕这个展开
- 具体行动：改变身边的一件事，改变一个工作流程，改变一个人
- 千万不要做那个不改变的人
- 短句收束，有余韵

```markdown
### 八、那句"拥抱它"，是什么意思

<img src="image/08-pioneer.webp" height="300">
*我们是第一批开拓者*

[正文 600 字]

---

### 关于作者

<img src="image/author_avatar_andy.png" height="200">

**老雷（Andy）**，明道云 & Nocoly CMO，SaaS 行业从业十余年。骨子里是个产品人和技术迷，乔布斯的信徒，相信好的产品能改变世界。深度关注 AI、商业与科技趋势，目前在深度使用和实践 Claude Code，专注探索 AI 如何重塑产品形态和商业逻辑。不聊概念，只聊真实发生的事。
```

- [ ] **Step 3: 验证总字数**

```bash
wc -m /Users/andy/Documents/articles/ai-employment-panman/article.md
```
Expected: 中文字符数约 4500-5500

- [ ] **Step 4: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/article.md
git commit -m "wip: article sections 7-8 + author bio"
```

---

## Task 9: 写图片说明文档 image_describe.md

**Files:**
- Create: `ai-employment-panman/image_describe.md`

- [ ] **Step 1: 写 image_describe.md**

```markdown
# 图片说明

## 01-panman.webp
**含义**：盯盘人的核心意象——人不再是执行者，而是监督者。
**与文章的关系**：对应第一节，视觉化"盯盘人"这个核心概念。

## 02-industrial.jpg
**含义**：工业革命时期工厂，工人在机器旁劳作。
**与文章的关系**：第二节历史叙述的视觉锚点，呈现上一次技术革命对劳动形态的冲击。

## 03-office-1990s.jpg
**含义**：1990年代办公室，排列整齐的工位和早期电脑。
**与文章的关系**：第三节互联网时代的视觉对应，打字员/文员时代的终结。

## 04-ai-wave.jpg
**含义**：AI 浪潮冲击就业市场的抽象示意。
**与文章的关系**：第四节，配合 Klarna 等企业用 AI 替代人工的数据。

## 05-busier.webp
**含义**：时间轴显示每次工具升级后人反而更忙的规律。
**与文章的关系**：第五节，反直觉核心论点的视觉化。

## 06-jobs.jpg
**含义**：乔布斯演讲/思考照片。
**与文章的关系**：第六节，引出"品位"论点，乔布斯是品位的最佳代言人。

## 07-tool-matrix.webp
**含义**：工具选择矩阵，价格×质量两轴，标注 MiniMax 和 Claude Code 位置。
**与文章的关系**：第七节，实操建议的直观呈现。

## 08-pioneer.webp
**含义**：站在数据浪潮之上的开拓者，前方是开阔的地平线。
**与文章的关系**：第八节收束，情感高点——我们是第一批开拓者。
```

- [ ] **Step 2: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/image_describe.md
git commit -m "add: image description documentation"
```

---

## Task 10: 写英文版 article-en.md

**Files:**
- Create: `ai-employment-panman/article-en.md`

- [ ] **Step 1: 翻译并意译为英文**

基于 article.md 完成后的中文版本进行意译，保留叙事语气，使用 WRITING.md 中的英文作者身份：
- 标题参考：《The Dashboard Watcher》
- 副标题：When AI Handles Most of the Execution, Where Does Human Value Go?
- 英文语气：conversational, direct, personal — "I taught my colleague Claude Code last week..."
- 乔布斯引用直接用英文原话："They have no taste."
- 文末使用英文作者介绍模板（见 WRITING.md）

格式要求：
```markdown
<img src="cover.png">

# The Dashboard Watcher

> When AI handles most of the execution, where does human value go?

---

### I. The Birth of the Dashboard Watcher

[正文意译]

<img src="image/01-panman.webp" height="300">
*When AI takes over execution, you just watch the dashboard*

---
[以此类推，八节结构与中文版对应]
```

- [ ] **Step 2: Commit**

```bash
cd /Users/andy/Documents/articles
git add ai-employment-panman/article-en.md
git commit -m "add: English version article-en.md"
```

---

## Task 11: 生成小红书组图

**Files:**
- 小红书图片输出到独立目录（由 baoyu-xhs-images skill 决定路径）

- [ ] **Step 1: 调用 baoyu-skills:baoyu-xhs-images skill**

参数：
- 文章内容：`ai-employment-panman/article.md`
- 风格：notion 手绘
- 张数：9 张（1封面 + 8内容图）
- 每张核心观点：
  1. **封面**：AI 来了，你的工作会消失吗？（引发好奇）
  2. **图2**：他用 Claude Code 做了一件不可思议的事（场景钩子）
  3. **图3**：历史告诉我们：每次革命，都有人消失，都有新人崛起
  4. **图4**：这次不同：AI 冲的是创意执行，不只是体力
  5. **图5**：反直觉：AI 来了我更忙了（不是坏事）
  6. **图6**：执行变廉价了，品位才是稀缺资产
  7. **图7**：乔布斯说：微软没有品位（这句话在 AI 时代更值钱）
  8. **图8**：工具建议：一个最便宜 + 一个最强
  9. **图9**：千万不要做那个不改变的人

- [ ] **Step 2: 确认图片生成完毕，记录路径**

- [ ] **Step 3: 如输出有问题，重新调整 prompt 重试**

---

## Task 12: 写 promotion.md

**Files:**
- Create: `ai-employment-panman/promotion.md`

- [ ] **Step 1: 写推广文案**

```markdown
# 推广文案 — 盯盘人

---

## 微信公众号

**标题备选（A/B测试）**：
- A: 《盯盘人》
- B: 《你以后只需要盯盘》
- C: 《AI 来了，你只需要盯盘》

**摘要**（发布命令 --summary 参数用）：
一个同事用 Claude Code 做了一件不可思议的事，然后他问我：以后人都不需要工作了？我说：你就拥抱它就行了。他当时的表情，既诧异又困惑。

---

## 微信朋友圈

昨天教了同事学 Claude Code。

他做出来之后，第一个反应是：这也太强了吧，以后人都不需要工作了？

我说：你就拥抱它就行了。

他的表情，既诧异，又困惑，想不明白。

新文章就是在解释这件事。

🔗 [文章链接]

---

## 微信群

【新文章】《盯盘人》

当 AI 接管了大部分执行性工作，人的价值往哪里放？

不是鸡汤，是逻辑推导 + 历史验证 + 实操建议。

约 5000 字，值得认真读一遍。

---

## 小红书

**标题**：AI 来了，你只需要"盯盘"就够了吗？

**正文**：
同事用 Claude Code 做了一个销售跟进自动化系统
以前：一个个催人、容易漏、不知道何时跟进
现在：AI 自动补信息、自动排优先级、自动规划时间
他只需要"盯盘"

他问我：以后人都不需要工作了？
我说：你就拥抱它就行了

但他当时的表情：诧异 + 困惑 + 想不明白

这篇文章就是在解释"拥抱它"是什么意思 👇

核心观点：
✅ AI 不会消灭工作，只会换门票
✅ 执行变廉价，品位才是稀缺资产
✅ 工具建议：一个最便宜 + 一个最强
✅ 千万不要做那个不改变的人

**标签**：#AI #Claude #人工智能 #职场 #效率 #Claude Code #未来工作

---

## 抖音

**口播稿（30秒）**：
上周我教一个同事学了 Claude Code，
他做出来之后问了我一个问题：
"以后人都不需要工作了，人去干啥？"
我说："你就拥抱它就行了。"
他当时的表情，我记得特别清楚，
既诧异，又困惑。

关于 AI 和就业，我想认真讲三件事：
第一，历史一直在重演，这次只是更快；
第二，执行变便宜了，品位才是稀缺资产；
第三，工具就用两个：一个最便宜，一个最强。

---

## Twitter/X

My colleague just built something incredible with Claude Code.

First thing he said: "Does this mean humans won't need to work anymore?"

Me: "Just embrace it."

His face: confused + slightly scared.

New post on why that answer is actually correct 👇

Key points:
→ AI doesn't eliminate work, it changes the entry ticket
→ When execution gets cheap, taste becomes scarce
→ Don't be the person who refuses to change

[link]

---

## 发布检查清单

- [ ] article.md 已完成，字数约 5000 字
- [ ] article-en.md 已完成
- [ ] cover.png 已生成（2.35:1）
- [ ] 8 张正文配图已到位
- [ ] 小红书组图已生成（9张）
- [ ] image_describe.md 已写完
- [ ] promotion.md 写完（本文件）
- [ ] 代码已 push 到 GitHub（不含 promotion.md）
- [ ] 微信公众号发布完成
- [ ] 小红书发布完成
```

- [ ] **Step 2: 确认 promotion.md 未被 git 追踪**

```bash
cat /Users/andy/Documents/articles/.gitignore | grep promotion
```
Expected: `promotion.md` 在 .gitignore 中

---

## Task 13: 最终审核

- [ ] **Step 1: 通读中文全文**

检查清单：
- 开篇是否从具体小场景切入（不从大道理开始）？
- 有无"不是……而是……"句式？（禁止）
- 有无冒号强调法？（禁止）
- 历史段落有无足够的画面感和细节？
- 乔布斯引用是否意译自然，没有生硬直译？
- 结尾是否用短句收束，有余韵？
- 封面图是否在 `<img src="cover.png">` 位置？
- 所有正文图片是否用 `![描述](路径)` Markdown 格式？（封面例外）
- 字数约 5000？

- [ ] **Step 2: 通读英文全文**

检查：语气是否自然、conversational？有无生硬中式英语？

- [ ] **Step 3: 确认所有图片文件存在**

```bash
ls /Users/andy/Documents/articles/ai-employment-panman/image/
```

- [ ] **Step 4: 最终 push 到 GitHub**

```bash
cd /Users/andy/Documents/articles
git push origin main
```

---

## Task 14: 发布微信公众号

**Files:** 无新文件

- [ ] **Step 1: 调用 baoyu-skills:baoyu-post-to-wechat skill**

发布命令（在文章目录内执行）：
```bash
cd /Users/andy/Documents/articles/ai-employment-panman
```
然后调用 skill，参数：
- markdown: `article.md`
- theme: `default`
- author: `老雷`
- summary: `一个同事用 Claude Code 做了一件不可思议的事，然后他问我：以后人都不需要工作了？我说：你就拥抱它就行了。他当时的表情，既诧异又困惑。`

- [ ] **Step 2: 封面图**

发布后在公众号编辑器手动上传封面图（脚本不支持自动上传封面），选用 `image/cover.png`。

- [ ] **Step 3: 预览确认排版正常后发布**

---

## Task 15: 发布小红书

- [ ] **Step 1: 调用 baoyu-skills:baoyu-xhs-images 已生成的组图**

确认 9 张图片已就位。

- [ ] **Step 2: 调用 mcp__xiaohongshu-mcp__publish_content**

参数：
- 标题：`AI 来了，你只需要"盯盘"就够了吗？`
- 正文：使用 promotion.md 中小红书部分的正文
- 图片：9张组图
- 标签：`#AI #Claude #人工智能 #职场 #效率 #Claude Code #未来工作`

- [ ] **Step 3: 确认发布成功**

---

## 完成标志

所有 15 个 Task 的 checkbox 全部勾选，微信公众号和小红书均已发布，GitHub 已 push。
