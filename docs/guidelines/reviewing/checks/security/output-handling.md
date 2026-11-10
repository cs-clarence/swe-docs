# Checks: output handling

Verifies [authoring/output-handling](../../../authoring/security/output-handling.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is data encoded for each destination context? | [encode for the destination](../../../authoring/security/output-handling.md#encode-for-the-destination) | Medium |
| Is encoding done at output rather than at storage? | [encode at the point of output](../../../authoring/security/output-handling.md#encode-at-the-point-of-output) | Medium |
| Is untrusted data never reflected raw? | [do not echo untrusted data unmodified](../../../authoring/security/output-handling.md#do-not-echo-untrusted-data-unmodified) | High |
| Does output include only needed, permitted fields? | [send only what the consumer needs](../../../authoring/security/output-handling.md#send-only-what-the-consumer-needs) | Medium |
| Are format and encoding declared and consistent? | [keep output format stable and declared](../../../authoring/security/output-handling.md#keep-output-format-stable-and-declared) | Low |

## Blocking

Blocking: unencoded untrusted data in output and over-broad output of sensitive fields. Others are should fix.
