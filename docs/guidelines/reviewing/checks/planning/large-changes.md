# Checks: large changes

Verifies [planning/large-changes](../../../planning/large-changes.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each step leave the system working? | [split into steps that each leave the system working](../../../planning/large-changes.md#split-into-steps-that-each-leave-the-system-working) | Medium |
| Does the new path exist beside the old until the switch? | [build the new path beside the old](../../../planning/large-changes.md#build-the-new-path-beside-the-old) | High |
| Are old and new results compared before the switch? | [keep old and new in agreement](../../../planning/large-changes.md#keep-old-and-new-in-agreement) | High |
| Is the end state and remaining work stated? | [make the end state visible](../../../planning/large-changes.md#make-the-end-state-visible) | Medium |
| Is the old path removed after the switch? | [remove the old path](../../../planning/large-changes.md#remove-the-old-path) | Medium |
| Is the plan recorded before work starts? | [agree the plan before the first step](../../../planning/large-changes.md#agree-the-plan-before-the-first-step) | High |
| Can each step be undone or safely stopped? | [keep every step reversible or safe to stop](../../../planning/large-changes.md#keep-every-step-reversible-or-safe-to-stop) | High |

## Blocking

Blocking: a switch-over with no way back for High-risk work, and a migration with no defined end. Others are should fix.
