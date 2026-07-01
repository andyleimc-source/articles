Create a professional vertical infographic showing how five Claude Code forms interconnect with two billing lines.

## Image Specifications
- Type: Infographic — vertical interop relationship guide
- Layout: dense-modules variant — 3 horizontal bands stacked vertically (Top / Middle / Bottom)
- Style: hand-drawn-edu (hand-drawn wobble, soft pastel feel, paper texture) with **雷码工坊 brand palette** REPLACING the default macaron palette
- Aspect Ratio: 9:16 (portrait)
- Language: Simplified Chinese

## Brand Color Palette (FORCED)
- Background: 米白 #FAF7F0 (warm cream, very subtle paper grain)
- Title text & main outlines: 墨黑 #0E1116 (NOT pure black)
- Accent / signal / "好" 标记: 磷绿 #1AB87C (phosphor green)
- Body text: 石墨 #3A4151
- Secondary lines / muted: 雾蓝 #9CB4CC
- Optional shadow: 砖灰 #6E6259 (sparingly)

**FORBID**: purple gradient, neon, cyberpunk, teal/cyan tech, pure black text, warm orange/coral/red, photorealistic, 3D cartoon.

## Layout Structure (top to bottom, three horizontal bands)

### Header (top ~10%)
- Hand-lettered title in 墨黑 with slight wobble: **五形态怎么互通**
- Subtitle in 石墨: 订阅 / API 两条计费线 · 5 小时窗口共享池
- Tiny doodle decoration in 磷绿

### TOP BAND (~25%) — 订阅线 (Subscription billing line)
- Header label: 订阅线 · 共享 5 小时窗口
- Three pill-shaped tier badges in a horizontal row:
  - Pill 1: Pro $20 (light 雾蓝 fill, 墨黑 text)
  - Pill 2: Max $100 (磷绿 fill, white text)
  - Pill 3: Max $200 (深 磷绿 fill, white text)
- Below the pills, a wobble-drawn rounded "pool" container with text inside: 5 小时滚动窗口  ·  全形态共享
- Three tiny downward arrows (磷绿) drop from the pool into MIDDLE BAND

### MIDDLE BAND (~50%) — 五形态卡片 (5 forms in 2-row grid)
Each card is a rounded rectangle with wobble border. Inside each card: form name (大字 墨黑), then small status badges showing where its quota comes from.

Use 2 rows × 3 columns with the last cell empty (or used for a doodle).

Card 1: **CLI 终端**
- Status: ✓ 订阅 · ✓ API
- Note: 双线可用

Card 2: **Desktop App**
- Status: ✓ 订阅 · ✗ API
- Note: 仅订阅

Card 3: **Web 版**
- Status: ✓ 订阅 · ✓ 免费
- Note: 浏览器即开

Card 4: **IDE 扩展**
- Status: ✓ 订阅 · ✓ API
- Note: 继承 CLI

Card 5: **API + SDK**
- Status: ✗ 订阅 · ✓ API
- Note: 仅 API

(6th cell): a small doodle of a paper note saying "1M 上下文 全开" with a tiny sparkle

### BOTTOM BAND (~10%) — API 线 (API billing line)
- Header label: API 线 · 按量计费
- One single pill: API 按量 (磷绿 outline, 米白 fill, 墨黑 text)
- Two upward arrows (磷绿) point from this pill up into Card 1 (CLI) and Card 5 (API+SDK), labeled "按 token"

### Footer (~5%)
- Right side small text: 雷码工坊笔记
- Color: 石墨 #3A4151 at 60-70% opacity
- Sans-serif, no decoration, no border

## Style Guidelines (modified hand-drawn-edu)

- Slight hand-drawn wobble on all card borders, lines, dividers, arrows
- Hand-lettered title with organic strokes
- Body text in clear handwritten-print style, but legible
- Cards rounded rectangles with 1.5-2px wobbly border in 雾蓝
- Each card has a thin 磷绿 accent stripe on the LEFT edge
- Status badges: ✓ in 磷绿, ✗ in 雾蓝 (NOT red, never any red!)
- Arrows are simple hand-drawn curves with small triangle heads, in 磷绿
- Warm cream paper background with very subtle grain texture
- Calm composition, generous breathing room

## Critical Constraints (字形)

- **Chinese glyphs must render correctly, no garbled characters, no fake-looking CJK, kerning correct, all 简体中文**
- All visible text on the canvas must be one of these strings exactly. No other text strings, no fake URLs, no decorative gibberish:
  - 五形态怎么互通
  - 订阅 / API 两条计费线 · 5 小时窗口共享池
  - 订阅线 · 共享 5 小时窗口
  - Pro $20
  - Max $100
  - Max $200
  - 5 小时滚动窗口  ·  全形态共享
  - CLI 终端
  - Desktop App
  - Web 版
  - IDE 扩展
  - API + SDK
  - ✓ 订阅 · ✓ API
  - ✓ 订阅 · ✗ API
  - ✓ 订阅 · ✓ 免费
  - ✗ 订阅 · ✓ API
  - 双线可用 / 仅订阅 / 浏览器即开 / 继承 CLI / 仅 API
  - 1M 上下文 全开
  - API 线 · 按量计费
  - API 按量
  - 按 token
  - 雷码工坊笔记
- Maximum 4 hand-drawn primary colors (米白 bg, 墨黑 outline, 磷绿 accent, 雾蓝 secondary). 石墨 only for body text.
- No purple, no neon, no glow, no 3D, no photo, no stock illustration, no warm orange.
- Do NOT draw any complex crossing lines between cards. Connections shown only by tier-pill → pool → middle-grid (downward) and bottom-pill → CLI/API+SDK cards (upward); no other arrows.
