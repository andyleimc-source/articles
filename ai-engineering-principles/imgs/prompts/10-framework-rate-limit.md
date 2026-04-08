---
illustration_id: "10"
type: framework
style: notion
---

限流与并发控制 Rate Limiting - Concurrency Control

STRUCTURE: funnel/valve control diagram

LEFT: Multiple request arrows coming in simultaneously (5-6 arrows labeled "请求 Request")

CENTER: Large valve/semaphore control icon — a circle with a dial or gate, labeled:
"Semaphore(3)
最多3个并发
Max 3 concurrent"

RIGHT: Only 3 arrows pass through to "API" box

BELOW API box: "HAP API" with a health indicator (green dot = healthy)

BELOW THAT: "429 Too Many Requests" shown as prevented (with shield/block icon)

BOTTOM annotation: "--gemini-concurrency 3" in code style
Second annotation: "RPD 追踪 RPD tracking: 2,340/10,000 今日用量"

COLORS:
- Background: white (#FFFFFF)
- Left incoming arrows: various colors, slightly messy
- Valve/semaphore: bold dark (#333333) with orange highlight (#FF8A65)
- 3 passing arrows: clean green (#43A047)
- Blocked arrows: fade out or dashed (#9E9E9E)
- API box: soft blue (#E3F2FD)
- 429 block: red shield (#E53935)
- Text: near-black (#1A1A1A)

STYLE: Notion minimalist hand-drawn. Clear funnel or valve metaphor. Bold arrows showing flow control.

Text should be large and prominent, handwritten-style. Clean composition with generous white space.
ASPECT: 16:9
