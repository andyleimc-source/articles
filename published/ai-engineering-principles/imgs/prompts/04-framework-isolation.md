---
illustration_id: "04"
type: framework
style: notion
---

隔离性 Isolation - Parallel Independent Tasks

STRUCTURE: horizontal parallel lanes

TOP: Label "Pipeline 主流程 Main Process" — wide horizontal bar

BELOW: 5 vertical parallel task lanes (like swimming lanes):
- Lane 1: 工作表A — green checkmark at bottom ✓
- Lane 2: 工作表B — green checkmark ✓  
- Lane 3: 工作表C — RED X at bottom ✗, label "失败 Failed" but dashed border showing it's contained
- Lane 4: 工作表D — green checkmark ✓
- Lane 5: 工作表E — green checkmark ✓

Each lane has a try/catch bubble around it (dashed rounded rectangle border)

ANNOTATION below Lane 3: "失败隔离在此 Failure contained here"
ANNOTATION bottom: "4/5 成功，1 失败不扩散 4/5 succeed, 1 failure doesn't spread"

COLORS:
- Background: white (#FFFFFF)
- Top bar: soft blue (#E3F2FD)
- Success lanes: very light green (#F1F8E9)
- Failed lane: very light red (#FFF0F0), dashed red border
- Checkmarks: green (#43A047)
- X mark: red (#E53935)
- Try/catch dashed boxes: gray (#9E9E9E)
- Text: near-black (#1A1A1A)

STYLE: Notion minimalist hand-drawn. Clear lane separators. Dashed lines for isolation boundaries.

Text should be large and prominent. Clean composition with generous white space.
ASPECT: 16:9
