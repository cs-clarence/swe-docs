# Checks: large changes

Verifies [planning/large-changes](../../../planning/large-changes.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does the new path exist beside the old until the switch? | [build the new path beside the old](../../../planning/large-changes.md#build-the-new-path-beside-the-old) | High |
| Are old and new results compared before the switch? | [keep old and new in agreement](../../../planning/large-changes.md#keep-old-and-new-in-agreement) | High |
| Is the end state and remaining work stated? | [make the end state visible](../../../planning/large-changes.md#make-the-end-state-visible) | Medium |
| Is the old path removed after the switch? | [remove the old path](../../../planning/large-changes.md#remove-the-old-path) | Medium |

## Blocking

Blocking: a switch-over with no way back for High-risk work, and a migration with no defined end. Others are should fix.
