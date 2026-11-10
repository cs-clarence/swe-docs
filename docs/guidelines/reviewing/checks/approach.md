# Checks: approach

Verifies [authoring/approach](../../authoring/approach.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Were the repository's instructions and overrides applied? | [check local rules first](../../authoring/approach.md#check-local-rules-first) | Low |
| Does the change fit current behavior, callers, and tests, as the author checked them? | [understand before changing](../../authoring/approach.md#understand-before-changing) | Medium |
| Is the goal and what the change will not touch stated? | [define the scope](../../authoring/approach.md#define-the-scope) | Low |
| Does the change touch only what the goal requires, and fix the cause rather than the symptom? | [make the smallest sufficient change](../../authoring/approach.md#make-the-smallest-sufficient-change) | Low |
| Is unrelated work kept out of the change? | [separate unrelated work](../../authoring/approach.md#separate-unrelated-work) | Low |
| Is observable behavior unchanged in a refactor? | [preserve behavior in refactors](../../authoring/approach.md#preserve-behavior-in-refactors) | Medium |
| Is there evidence the change works, scaled to the tier, and for a fix that the failure existed before and is gone? | [verify the result](../../authoring/approach.md#verify-the-result) | Low |
| Does the description say what changed, why, how it was verified, and what remains unverified? | [explain the result](../../authoring/approach.md#explain-the-result) | Low |

## Blocking

Blocking: a refactor that changes behavior, no verification where the tier requires it, and unrelated changes that make the change unreviewable. Others are should fix. Review priority and finding classes are in [process](../process.md).
