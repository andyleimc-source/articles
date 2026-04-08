---
illustration_id: "03"
type: flowchart
style: notion
---

步间校验 Inter-step Validation - Gate Flow

Layout: left-to-right with validation gates between steps

STEPS:
1. AI 输出 AI Output — raw data block
2. [GATE 1] 代码校验 Code Check — diamond shape, "合法?" Valid?
   - Yes → pass through
   - No → ✗ 丢弃 Discard (drops down, exits flow)
3. 下一步 Next Step — receives only clean data
4. [GATE 2] 代码校验 Code Check — same pattern
5. 执行 Execute

ANNOTATION below: "校验用代码，快且确定性强 Code validation: fast and deterministic"

COLORS:
- Background: white (#FFFFFF)  
- AI output box: light blue (#E3F2FD)
- Gate diamonds: warm yellow (#FFF9C4) with dark border
- Pass arrows: green (#43A047)
- Reject arrows: red (#E53935), pointing downward
- Discard labels: red text
- Step boxes: light gray (#F5F5F5)
- Text: near-black (#1A1A1A)

STYLE: Notion minimalist hand-drawn. Diamond decision shapes clearly drawn. Thick arrows. No gradients.

Text should be large and prominent, handwritten-style. Clean composition with generous white space.
ASPECT: 16:9
