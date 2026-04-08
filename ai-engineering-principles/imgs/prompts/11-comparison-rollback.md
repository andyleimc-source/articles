---
illustration_id: "11"
type: comparison
style: notion
---

回滚 Rollback - Two Recovery Strategies

Layout: forked path / decision tree

TOP: Pipeline failure event — box labeled "Pipeline 失败 Pipeline Failed ✗"

FORK: Arrow splits into two paths below

LEFT PATH - 默认策略 Default Strategy:
- Path label: "保留已成功 Keep successes"
- Below: 3 boxes, 2 green (✓ 已创建 Created), 1 gray (✗ 失败 Failed, skipped)
- Label: "局部成功，立即可用 Partial success, immediately usable"
- Footer: "默认行为 Default behavior"

RIGHT PATH - 回滚策略 Rollback Strategy (--rollback-on-failure):
- Path label: "--rollback-on-failure"
- Below: All boxes cleared/deleted (delete icon on each)
- Label: "全部清除，重新来 Clean slate"
- Footer: "要么全有，要么全无 All or nothing"

CENTER FORK: Bold Y-shape or fork icon

COLORS:
- Background: white (#FFFFFF)
- Failure box: light red (#FFF0F0)
- Left path: light green (#F0FFF0)
- Right path: light gray (#F5F5F5)
- Success boxes: green (#43A047)
- Failed/skipped box: gray (#9E9E9E)
- Delete icons: red (#E53935)
- Fork arrows: dark gray (#424242)
- Default label: green badge
- Rollback label: gray badge
- Text: near-black (#1A1A1A)

STYLE: Notion minimalist hand-drawn. Clear Y-fork branching. Simple boxes for created resources.

Text should be large and prominent, handwritten-style. Clean composition with generous white space.
ASPECT: 16:9
