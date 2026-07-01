Create a professional vertical infographic — a decision tree that guides the reader through 4 questions to land on the right Claude Code form.

## Image Specifications
- Type: Infographic — vertical decision tree / flowchart
- Layout: tree-branching variant (vertical Q→split→A flow)
- Style: hand-drawn-edu (hand-drawn wobble, soft pastel feel, paper texture) with **雷码工坊 brand palette** REPLACING the default macaron palette
- Aspect Ratio: 9:16 (portrait)
- Language: Simplified Chinese

## Brand Color Palette (FORCED)
- Background: 米白 #FAF7F0 (warm cream, very subtle paper grain)
- Title text & main outlines: 墨黑 #0E1116 (NOT pure black)
- Accent / "yes" path / final recommendation chips: 磷绿 #1AB87C
- Body text: 石墨 #3A4151
- Secondary lines / "no" path / branches: 雾蓝 #9CB4CC
- Optional shadow: 砖灰 #6E6259 (sparingly)

**FORBID**: purple gradient, neon, cyberpunk, teal/cyan tech, pure black text, warm orange/coral/red, photorealistic, 3D cartoon.

## Layout (top to bottom)

### Header (~10%)
- Hand-lettered title in 墨黑 with slight wobble: **决策树·4 个问题落地**
- Subtitle in 石墨: 跟着问一遍·选对你的形态
- Tiny doodle decoration in 磷绿

### Decision tree (~75%)

A vertical flowchart with 4 question diamonds, each branching left/right. Each diamond is a hand-drawn rounded rectangle (NOT a perfect diamond shape — keep the wobble). Connect with simple wobbly lines and small triangular arrowheads.

**Top level — Q1**:
Box (墨黑 outline, 米白 fill): 你写代码吗？
Two branches:
  - Left arrow labeled 不写 (in 雾蓝): leads to a 磷绿 result chip "→ Desktop App / Web 版"
  - Right arrow labeled 写 (in 磷绿): drops down to Q2

**Q2**:
Box: 习惯用终端吗？
Two branches:
  - Left labeled 不习惯: → 磷绿 chip "→ IDE 扩展"
  - Right labeled 习惯: drops down to Q3

**Q3**:
Box: 要不要长任务·后台跑？
Two branches:
  - Left labeled 不要: → 磷绿 chip "→ IDE 扩展 + Desktop"
  - Right labeled 要: drops down to Q4

**Q4**:
Box: 自己用·还是要嵌进产品？
Two branches:
  - Left labeled 自己用: → 磷绿 chip "→ CLI 终端"
  - Right labeled 嵌进产品: → 磷绿 chip "→ API + Agent SDK"

Branch arrows: "yes/继续往下" arrows in 磷绿 with thicker stroke; "短路出口" arrows in 雾蓝 thinner.

### Footer (~5%)
- Right side small text: 雷码工坊笔记
- Color: 石墨 #3A4151 at 60-70% opacity
- Sans-serif, no decoration, no border

## Style Guidelines (modified hand-drawn-edu)
- Slight hand-drawn wobble on all box borders, lines, arrows
- Hand-lettered title with organic strokes
- Body text in clear handwritten-print style, legible
- Question boxes: 米白 fill, 墨黑 wobble outline 1.5-2px
- Result chips (磷绿 fill, white text), pill-shaped, slight wobble
- Arrows are hand-drawn curves with small triangle heads
- Warm cream paper background with very subtle grain
- Calm, breathing layout — leave whitespace between question levels

## Critical Constraints (字形)

- **Chinese glyphs must render correctly, no garbled characters, no fake-looking CJK, kerning correct, all 简体中文**
- All visible text must be one of these strings exactly. No other text strings, no fake URLs, no decorative gibberish:
  - 决策树·4 个问题落地
  - 跟着问一遍·选对你的形态
  - 你写代码吗？
  - 不写
  - 写
  - → Desktop App / Web 版
  - 习惯用终端吗？
  - 不习惯
  - 习惯
  - → IDE 扩展
  - 要不要长任务·后台跑？
  - 不要
  - 要
  - → IDE 扩展 + Desktop
  - 自己用·还是要嵌进产品？
  - 自己用
  - 嵌进产品
  - → CLI 终端
  - → API + Agent SDK
  - 雷码工坊笔记
- Maximum 4 hand-drawn primary colors (米白 bg, 墨黑 outline, 磷绿 yes-path/result, 雾蓝 no-path). 石墨 only for body text.
- No purple, no neon, no glow, no 3D, no photo, no warm orange, no red.
- Keep the flow strictly vertical from top to bottom — no crossing lines.
