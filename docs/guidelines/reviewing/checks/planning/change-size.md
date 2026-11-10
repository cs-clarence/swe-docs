# Checks: change size

Verifies [planning/change-size](../../../planning/change-size.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is the change small enough to review as one unit, with one purpose? | [keep a change small enough to review](../../../planning/change-size.md#keep-a-change-small-enough-to-review) | Medium |
| Does each part of a split stand alone? | [split by purpose, not by file type](../../../planning/change-size.md#split-by-purpose-not-by-file-type) | Medium |
| Are restructuring, behavior change, and cleanup in separate parts? | [put preparation first](../../../planning/change-size.md#put-preparation-first) | Low |
| Are parts that cannot stand alone kept together, with the reason stated? | [keep together what only works together](../../../planning/change-size.md#keep-together-what-only-works-together) | Medium |
| Are mechanical changes separate from logic, with how they were made or checked? | [separate mechanical change from logic](../../../planning/change-size.md#separate-mechanical-change-from-logic) | Medium |
| Is oversized work planned as safe steps? | [plan work too big for one change](../../../planning/change-size.md#plan-work-too-big-for-one-change) | Medium |

## Blocking

A change too large to review is a reason to ask for a split, not to approve what was not examined ([review process](../../process.md#responsibilities)). Others are should fix.
