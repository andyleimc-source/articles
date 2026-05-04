Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: binary-comparison (Before-After variant)
- **Style**: technical-schematic (Blueprint variant)
- **Aspect Ratio**: 16:9
- **Language**: zh + English mix

## Core Principles

- Follow the binary-comparison layout precisely: vertical divider, mirrored left/right panels
- Apply technical-schematic Blueprint style: deep blue, white technical line work, drafting aesthetic
- Keep text minimal and use exact strings provided — DO NOT paraphrase or generate alternative wording
- Crisp text, no glyph errors

## Text Requirements (use these strings EXACTLY)

- Main title (centered, top, white, all caps): `REFACTOR · ABSOLUTE RULES → DECISION RULES`
- Subtitle (centered, lighter): `把"砸到模型脸上的规则"改写成"教模型判断的条件"`

**Left panel header**: `❌ OLD WAY · GPT-5 ERA`
**Left panel filename tag**: `system.prompt.txt — 5,247 lines`
**Left panel content** (each on its own line, monospace, with red `−` minus marker on the left of each line):
```
ALWAYS respond in Chinese.
NEVER include code unless asked.
You MUST cite sources.
You MUST NOT speculate.
IMPORTANT: be concise.
CRITICAL: never invent facts.
Under NO circumstances invent
  function names.
ALWAYS follow JSON schema.
... continues for 200+ lines
```
Highlight the words `ALWAYS`, `NEVER`, `MUST`, `MUST NOT`, `IMPORTANT`, `CRITICAL`, `NO` in **bold red/rose**.
**Left panel footer caption (small, italic, rose)**: `把规则砸在模型脸上 → 边界情况下变得机械`

**Right panel header**: `✅ NEW WAY · GPT-5.5 ERA`
**Right panel filename tag**: `system.prompt.txt — 14 lines`
**Right panel content** (each on its own line, monospace, with green `+` plus marker on the left):
```
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
Highlight the word `If` (both occurrences) in **amber/yellow** to emphasize the conditional/decision-rule nature.
**Right panel footer caption (small, italic, green)**: `教模型判断 → 在边界情况下做出更聪明的选择`

## Center divider

A central amber arrow `→` between the two panels, with a small chip/pill labeled `refactor` in amber.

## Bottom summary band

Two centered text lines at the bottom:
- Line 1 (white, weight 600): `Decision rules > Absolute rules · Outcome description > Process instructions`
- Line 2 (smaller, lighter): `决策规则 优于 绝对指令 · 描述结果 优于 指令过程`

## Layout Guidelines (binary-comparison)

- Sharp vertical divider down the middle
- Left half tinted slightly red, right half tinted slightly green
- Both panels are rendered as **stylized code-editor windows**: rounded rectangles with three traffic-light dots (red/yellow/green) at the top-left of each panel header
- Mirrored sizing — left and right panels equal width and height
- Center arrow positioned at vertical midpoint of both panels

## Style Guidelines (technical-schematic, Blueprint variant)

- Deep blueprint blue page background (#0F2A44), faint white grid pattern
- Left panel: red-tinted background `#2A0F0F`, rose `#F87171` border + accents
- Right panel: green-tinted background `#0F2A1F`, emerald `#34D399` border + accents
- Center arrow + refactor pill: amber `#F59E0B`
- All text in JetBrains-Mono-style monospace
- Crisp 1px line work, technical drafting feel, NO photorealism, NO 3D effects

## Strict prohibitions

- No purple gradients
- No glowing particles
- No robots, faces, mascots
- No decorative confetti or illustrative noise
- No misspelled English words
- DO NOT replace any of the provided text strings with paraphrases

## Mood

A senior engineer's GitHub PR diff view, posted in a code review. Confident, instructional, exact.
