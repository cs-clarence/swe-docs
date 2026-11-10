# Checks: releases and rollback

Verifies [authoring/releases-and-rollback](../../authoring/releases-and-rollback.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is there a stated way to undo the release? | [know how to undo before shipping](../../authoring/releases-and-rollback.md#know-how-to-undo-before-shipping) | Medium |
| Can the change be shipped off and enabled separately? | [separate shipping from enabling](../../authoring/releases-and-rollback.md#separate-shipping-from-enabling) | Medium |
| Is exposure staged for a High-risk change? | [expose gradually when risk is high](../../authoring/releases-and-rollback.md#expose-gradually-when-risk-is-high) | High |
| Does each step work alone, with the one before and after? | [order dependent changes so any step can stop](../../authoring/releases-and-rollback.md#order-dependent-changes-so-any-step-can-stop) | High |
| Are the failure signals named before release? | [decide the failure signals first](../../authoring/releases-and-rollback.md#decide-the-failure-signals-first) | Medium |
| Is there a defined watch period after release? | [watch after release](../../authoring/releases-and-rollback.md#watch-after-release) | Medium |
| Does rollback keep data written since release? | [do not let rollback lose data](../../authoring/releases-and-rollback.md#do-not-let-rollback-lose-data) | High |
| Can the running version be identified? | [make the running version identifiable](../../authoring/releases-and-rollback.md#make-the-running-version-identifiable) | Low |
| Was the rollback exercised for a High-risk change? | [rehearse the rollback for high-risk changes](../../authoring/releases-and-rollback.md#rehearse-the-rollback-for-high-risk-changes) | High |

## Blocking

Blocking: a High-risk release with no way to undo it and no stated reason and alternative, and a rollback that loses data. Others are should fix.
