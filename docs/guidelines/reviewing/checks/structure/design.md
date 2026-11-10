# Checks: design

Verifies [authoring/design](../../../authoring/structure/design.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each new unit do one nameable thing? | [one responsibility](../../../authoring/structure/design.md#give-each-unit-one-responsibility) | Medium |
| Is composition used rather than deep inheritance, per repo idiom? | [composition](../../../authoring/structure/design.md#prefer-composition) | Medium |
| Can illegal states be represented? | [invalid states](../../../authoring/structure/design.md#make-invalid-states-hard-to-represent) | Medium |
| Does shared mutable state have a single owner? | [shared state](../../../authoring/structure/design.md#limit-shared-mutable-state) | High |
| Are side effects kept at the edges? | [side effects](../../../authoring/structure/design.md#isolate-side-effects) | Medium |

## Blocking

Blocking: shared mutable state with no clear owner. Others are should fix or optional.
