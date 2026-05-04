# Diagram: Refactor — From ALWAYS/NEVER to Decision Rules

## Concept

A wide editorial infographic, **16:9 aspect ratio**, dark technical-blog aesthetic, designed in the style of a **GitHub Pull Request diff view**. Two side-by-side code panels showing a "before / after" refactor of a system prompt.

## Layout

Two large code-editor panels side by side, separated by a centered **arrow with a `refactor` pill label**.

**Left panel — "❌ Old way (GPT-5 era)"**
- Header tab in dark red `#7f1d1d` saying `❌ Old way (GPT-5 era)`
- Code-editor frame with three traffic-light dots and filename: `system.prompt.txt — 5,247 lines`
- Background: very dark red-tinted `#1a0e0e`, red `#7f1d1d` border
- Each line of code has a **left gutter showing `−` minus markers** (red, weight 700) and a **subtle red highlight strip** behind the line, like a GitHub diff "removed line"
- Code content (English, monospace):
  ```
  SYSTEM PROMPT:

  ALWAYS respond in Chinese.
  NEVER include code unless
    the user explicitly asks.
  You MUST cite sources.
  You MUST NOT speculate.
  IMPORTANT: be concise.
  CRITICAL: never make up facts.
  Under NO circumstances should
    you invent function names.
  ALWAYS follow JSON schema.

  // ...continues for 200+ lines
  ```
- Bold red highlight on the words: `ALWAYS`, `NEVER`, `MUST`, `MUST NOT`, `NO`, `IMPORTANT`, `CRITICAL`
- Bottom italic caption (red, small): `把规则砸在模型脸上 → 边界情况下变得机械`

**Right panel — "✅ New way (GPT-5.5 era)"**
- Header tab in dark green `#064e3b` saying `✅ New way (GPT-5.5 era)`
- Code-editor frame with traffic-light dots and filename: `system.prompt.txt — 14 lines`
- Background: very dark green-tinted `#0a1f17`, green `#34d399` border
- Each line has a **left gutter `+` plus marker** (green) and **subtle green highlight strip**
- Code content:
  ```
  SYSTEM PROMPT:

  A good answer:
    - is in Chinese
    - cites real sources
    - stays concise

  If the user asks a
  conceptual question,
  answer in prose.

  If they ask "how to",
  include a minimal
  code example.
  ```
- The word `If` should be **highlighted amber `#fbbf24`** to emphasize the conditional / decision-rule nature
- Bottom italic caption (green, small): `教模型判断 → 在边界情况下做出更聪明的选择`

## Center connector

Between the two panels:
- A horizontal arrow `→` in **amber `#fbbf24`**, weight 3px, with arrowhead
- Below the arrow: a **small amber-bordered pill / chip** containing the word `refactor` in amber text

## Title (top of image)

- **Title** (centered, white, sans-serif, weight 700): `Refactor: 从 ALWAYS / NEVER 到决策规则`
- **Subtitle** (centered, smaller, slate `#94a3b8`): `把"砸到模型脸上的规则"改写成"教模型判断的条件"`

## Bottom summary

Two small lines of text, centered at the bottom:
- Line 1 (light slate, weight 600): `Decision rules > Absolute rules · Outcome description > Process instructions`
- Line 2 (smaller, grey): `决策规则 优于 绝对指令 · 描述结果 优于 指令过程`

## Color palette

- Page background: very dark navy `#0f172a` with subtle dot-grid texture
- Left panel: red-tinted `#1a0e0e` background, `#7f1d1d` border, `#fecaca` text
- Right panel: green-tinted `#0a1f17` background, `#34d399` border, `#a7f3d0` text
- Highlights: red `#fb7185` (rules), amber `#fbbf24` (conditions, refactor pill), emerald `#34d399` (positive)
- All code text in **JetBrains Mono** style monospace

## Strict prohibitions

NO purple gradients. NO glowing particles. NO 3D effects. NO robots / hands / faces. NO floating geometric shapes for decoration. NO marketing-style hero. Keep it strictly **GitHub-PR-diff aesthetic**, flat and technical.

## Mood

Confident, technical, instructional. Looks like a real diff a senior engineer would post in a code review.
