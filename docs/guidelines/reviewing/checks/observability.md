# Checks: observability

Verifies [authoring/observability](../../authoring/observability.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Can one request or job be traced from the output? | [emit what operators need to diagnose](../../authoring/observability.md#emit-what-operators-need-to-diagnose) | Medium |
| Are levels used consistently? | [use levels consistently](../../authoring/observability.md#use-levels-consistently) | Low |
| Is sensitive data absent from telemetry? | [keep sensitive data out of telemetry](../../authoring/observability.md#keep-sensitive-data-out-of-telemetry) | Low |
| Is output structured, with a correlation identifier? | [use structured, correlatable output](../../authoring/observability.md#use-structured-correlatable-output) | Medium |
| Is telemetry bounded and non-fatal? | [do not let telemetry break the system](../../authoring/observability.md#do-not-let-telemetry-break-the-system) | Medium |

## Blocking

Blocking: sensitive data in telemetry and unbounded log volume. Others are optional.
