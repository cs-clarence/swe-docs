# Checks: performance

Verifies [authoring/performance](../../authoring/performance.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Was the bottleneck measured? | [measure before optimizing](../../authoring/performance.md#measure-before-optimizing) | Medium |
| Is the target stated? | [state the target](../../authoring/performance.md#state-the-target) | Medium |
| Are accidental costs such as queries in loops avoided? | [avoid known accidental costs](../../authoring/performance.md#avoid-known-accidental-costs) | Medium |
| Are inputs, queues, and results bounded? | [bound resource use](../../authoring/performance.md#bound-resource-use) | Medium |
| Is improvement shown by measurement? | [prove the improvement](../../authoring/performance.md#prove-the-improvement) | Medium |
| Is complexity justified by evidence? | [keep clarity unless measurement justifies otherwise](../../authoring/performance.md#keep-clarity-unless-measurement-justifies-otherwise) | Low |

## Blocking

Blocking: unbounded resource use on outside-controlled input. Unmeasured micro-optimizations are should fix.
