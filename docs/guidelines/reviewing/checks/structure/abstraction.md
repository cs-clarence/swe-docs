# Checks: abstraction

Verifies [authoring/abstraction](../../../authoring/structure/abstraction.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is each new abstraction backed by real uses or a genuine boundary? | [on evidence](../../../authoring/structure/abstraction.md#abstract-on-evidence) | Medium |
| Is shared code forced to serve cases that may diverge? | [duplication](../../../authoring/structure/abstraction.md#prefer-duplication-to-the-wrong-abstraction) | Medium |
| Does the interface survive swapping the implementation? | [hide what varies](../../../authoring/structure/abstraction.md#hide-what-varies-expose-what-is-stable) | Medium |
| Are guarantees, assumptions, and failure modes stated? | [contract](../../../authoring/structure/abstraction.md#state-the-contract) | Medium |
| Must callers know the implementation to use it correctly? | [leaks](../../../authoring/structure/abstraction.md#do-not-leak-implementation-details) | Medium |
| Does each unit stay at one level of abstraction? | [one level](../../../authoring/structure/abstraction.md#keep-one-level-of-abstraction-per-unit) | Low |
| Are names about purpose rather than mechanism? | [naming](../../../authoring/structure/abstraction.md#name-for-purpose) | Low |
| Are there options, flags, or hooks nothing uses? | [speculative](../../../authoring/structure/abstraction.md#do-not-generalize-speculatively) | Medium |
| Does every layer add a boundary, translation, or simplification? | [thin layers](../../../authoring/structure/abstraction.md#keep-layers-thin-and-earning-their-place) | Medium |
| Is a widely used volatile dependency wrapped? | [volatile dependencies](../../../authoring/structure/abstraction.md#isolate-volatile-dependencies) | Medium |
| Is an abstraction with one fixed implementation or routine workarounds simplified? | [remove abstractions that no longer pay](../../../authoring/structure/abstraction.md#remove-abstractions-that-no-longer-pay) | Low |

## Blocking

Blocking: an abstraction that leaks in a way that makes callers incorrect, and public contracts added without stated guarantees. Premature or speculative abstraction in internal code is should fix.
