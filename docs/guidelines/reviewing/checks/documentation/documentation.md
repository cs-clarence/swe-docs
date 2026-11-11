# Checks: documentation

Verifies [authoring/documentation](../../../authoring/documentation/documentation.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does the document name its reader and purpose? | [write for a named reader](../../../authoring/documentation/documentation.md#write-for-a-named-reader) | Low |
| Were docs updated with the behavior they describe? | [update docs in the same change as behavior](../../../authoring/documentation/documentation.md#update-docs-in-the-same-change-as-behavior) | Medium |
| Is each fact described in one place? | [link instead of copying](../../../authoring/documentation/documentation.md#link-to-facts-instead-of-copying-them) | Low |
| Do examples work as written? | [make examples runnable](../../../authoring/documentation/documentation.md#make-examples-runnable) | Medium |
| Are purpose and limitations stated? | [document the why and the limits](../../../authoring/documentation/documentation.md#document-the-why-and-the-limits) | Low |
| Is sensitive data absent? | [keep sensitive data out of docs](../../../authoring/documentation/documentation.md#keep-sensitive-data-out-of-docs) | Low |

## Blocking

Blocking: sensitive data in docs, and docs that contradict changed behavior. Others are optional.
