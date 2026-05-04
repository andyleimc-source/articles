# Diagram: Four Generations of Prompt Engineering

## Concept

A wide editorial infographic, **16:9 aspect ratio**, dark technical-blog aesthetic. The image visually compares **four eras of prompt writing** across GPT model generations, arranged as **four columns from left to right**, getting visually **lighter, cleaner, and more spacious** as you move right.

The whole image should feel like a **technical documentation diagram from a developer blog** — like a screenshot you might find on the OpenAI engineering blog or a Hacker News post.

## Layout

A horizontal 4-panel comparison. Each panel is a stylized **code editor window** (rounded rectangle with the three traffic-light dots in the top-left corner — red, yellow, green — and a small filename label on the right of the title bar).

**Panel 1 — leftmost — "GPT-3 · 2021"**
- Filename: `prompt.txt`
- Filled densely with `Q:` / `A:` few-shot example pairs (English text, monospace). Show ~8-10 example pairs visually packed together.
- Color tone: **cool desaturated grey-blue text** on dark background.
- Bottom label: **"Few-shot example stacking"**

**Panel 2 — "GPT-4 · 2023"**
- Filename: `system.txt`
- Filled with: a top role line `You are a world-class expert...`, then XML-style tags like `<task>`, `<instructions>`, `<output_format>` with content inside. Show "Let's think step by step" and numbered reasoning steps. Include `<examples>` tag at the bottom.
- Color tone: **cyan/teal accent** on the XML tags.
- Bottom label: **"Role-play + CoT + XML tags"**

**Panel 3 — "GPT-5 · 2024"**
- Filename: `rules.md`
- Filled with rule-list style: `ROLE: Translator` then a wall of `ALWAYS use formal register.` / `NEVER add commentary.` / `You MUST output JSON only.` / `IMPORTANT: preserve meaning.` / `CRITICAL: handle edge cases.` / `Under NO circumstances...`. The keywords `ALWAYS`, `NEVER`, `MUST`, `IMPORTANT`, `CRITICAL` should be **bold red/rose color**, the rest in light grey.
- Border tint: **red/rose**, suggesting harshness.
- Bottom label: **"ALWAYS / NEVER rule lists"**

**Panel 4 — rightmost — "GPT-5.5 · 2026"**
- Filename: `prompt.txt`
- Almost empty. Just **three short lines** of text near the top:
  ```
  Translate to French.
  Formal register, JSON output.
  ```
- The rest of the panel is **mostly empty space**, with a small italic line in the middle: `— that's it. —`
- Color tone: **soft terminal-green accent**, calm and clean.
- Border tint: **green**.
- Bottom label: **"Outcome-first · minimal"**

## Between panels

Small subtle right-pointing arrows `→` between each panel.

## Below all four panels

A horizontal **density bar** showing density decreasing left to right. Four colored segments:
- Wide red segment under panel 1
- Slightly narrower amber segment under panel 2
- Wide orange segment under panel 3
- Tiny green segment under panel 4

Right end of the bar has a label `↓ getting thinner` (in small grey text).

## Title and subtitle (top of image)

- **Title** (top-left, white, sans-serif, weight 700): `Prompt 写法四代演化`
- **Subtitle** (small grey): `Four years, four prompt patterns — each generation needs less compensation from the user`

## Bottom summary text

Small centered grey text: `每一代模型变强 = 使用者代偿减少一层` / `Each generation grows smarter → users write less to compensate`

## Color palette

- Background: very dark navy `#0f172a` with a subtle dot grid texture
- Panel backgrounds: slate `#1e293b`
- Title bars on panels: near-black `#0a0a0a`
- Text: light slate `#cbd5e1` for code, white `#ffffff` for headers
- Accents: cyan `#22d3ee`, rose `#fb7185`, amber `#fbbf24`, emerald `#34d399`
- Use **JetBrains Mono** style monospace fonts for all code-like text

## Strict prohibitions

NO purple gradients. NO glowing particles for decoration. NO 3D effects. NO robots / faces / hands. NO floating geometric shapes. NO marketing-style hero illustrations. NO generic-AI tropes. Keep it **flat, technical, editorial**, like a real diagram in a developer blog post.

## Mood

Quiet, observational, slightly nostalgic. Shows the slow deflation of prompt engineering with calm authority.
