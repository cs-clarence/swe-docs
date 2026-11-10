# Checks: concurrency

Verifies [authoring/concurrency](../../authoring/concurrency.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is shared mutable state minimized? | [minimize shared mutable state](../../authoring/concurrency.md#minimize-shared-mutable-state) | High |
| Is shared state guarded by one documented mechanism? | [protect what must be shared](../../authoring/concurrency.md#protect-what-must-be-shared) | High |
| Does every wait have a timeout? | [bound waiting with timeouts](../../authoring/concurrency.md#bound-waiting-with-timeouts) | Medium |
| Can long work be cancelled and cleaned up? | [support cancellation](../../authoring/concurrency.md#support-cancellation) | Medium |
| Is correctness independent of timing? | [do not rely on timing or ordering](../../authoring/concurrency.md#do-not-rely-on-timing-or-ordering) | High |
| Are parallelism and queues bounded? | [bound parallelism and queues](../../authoring/concurrency.md#bound-parallelism-and-queues) | Medium |

## Blocking

Blocking: races on shared state, unbounded waits, and ordering assumptions without enforcement. Others are should fix.
