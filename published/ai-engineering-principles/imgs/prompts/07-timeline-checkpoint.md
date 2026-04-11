---
illustration_id: "07"
type: timeline
style: notion
---

断点续跑 Resume / Checkpoint - Recovery from Failure

DIRECTION: horizontal

TOP ROW - "没有 Checkpoint Without Checkpoint":
- Timeline: Step1 → Step2 → Step3 → ✗ CRASH → (restart symbol) → Step1 → Step2 → Step3...
- Long sad arrow showing having to restart from beginning
- Label: "从头重来 Start over"

BOTTOM ROW - "有 Checkpoint With Checkpoint":
- Timeline: Step1[💾] → Step2[💾] → Step3[💾] → ✗ CRASH → (resume symbol) → Step3...
- Each step has a small save/disk icon
- After crash, resumes from Step3, not Step1
- Label: "从断点继续 Resume from checkpoint"

CENTER DIVIDER: horizontal dashed line separating two scenarios

BOTTOM annotation: "每步输出持久化，不重复做已做的事 Persist each step output"

COLORS:
- Background: white (#FFFFFF)
- Top row (no checkpoint): light red tint (#FFF0F0) background
- Bottom row (with checkpoint): light green tint (#F0FFF0) background
- Crash marker: red X (#E53935)
- Checkpoint save icons: blue (#1976D2)
- Resume arrow: green (#43A047), bold
- Restart arrow: red (#E53935), thinner
- Text: near-black (#1A1A1A)

STYLE: Notion minimalist hand-drawn. Clear timeline dots and connecting lines. Simple save icon (floppy disk or cloud). No gradients.

Text should be large and prominent, handwritten-style. Clean composition with generous white space.
ASPECT: 16:9
