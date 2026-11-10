# Checks: resilience

Verifies [authoring/resilience](../../authoring/resilience.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does every remote call have a timeout? | [set a timeout on every remote call](../../authoring/resilience.md#set-a-timeout-on-every-remote-call) | Medium |
| Do retries back off, with jitter and a bound? | [retry with backoff and a limit](../../authoring/resilience.md#retry-with-backoff-and-a-limit) | Medium |
| Is there a way to fail fast on a failing dependency? | [stop calling a failing dependency](../../authoring/resilience.md#stop-calling-a-failing-dependency) | High |
| Is behavior without each dependency defined? | [degrade deliberately](../../authoring/resilience.md#degrade-deliberately) | High |
| Is accepted load bounded? | [limit load you accept](../../authoring/resilience.md#limit-load-you-accept) | Medium |
| Are dependency failures tested? | [test failure modes](../../authoring/resilience.md#test-failure-modes) | Medium |

## Blocking

Blocking: remote calls without timeouts and unbounded retries. Others are should fix.
