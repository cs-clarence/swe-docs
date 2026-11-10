# Checks: refactoring

Verifies [authoring/refactoring](../../../authoring/structure/refactoring.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Do tests cover the behavior being preserved? | [pin behavior before restructuring](../../../authoring/structure/refactoring.md#pin-behavior-before-restructuring) | Medium |
| Is each step small and verified? | [change in small, verifiable steps](../../../authoring/structure/refactoring.md#change-in-small-verifiable-steps) | Medium |
| Is the refactor free of behavior changes? | [keep structure and behavior changes apart](../../../authoring/structure/refactoring.md#keep-structure-and-behavior-changes-apart) | Low |
| Is the purpose stated? | [refactor for a stated purpose](../../../authoring/structure/refactoring.md#refactor-for-a-stated-purpose) | Low |
| Is unrelated cleanup left out? | [stop when the purpose is met](../../../authoring/structure/refactoring.md#stop-when-the-purpose-is-met) | Low |
| Are all callers and references updated? | [update every caller and reference](../../../authoring/structure/refactoring.md#update-every-caller-and-reference) | Medium |

## Blocking

Blocking: behavior changes hidden in a refactor, and a refactor without tests covering the changed code. Others are should fix.
