# Checks: release-notes

Verifies [authoring/documentation/release-notes](../../../authoring/documentation/release-notes.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Are entries written as user impact? | [write for the user's impact](../../../authoring/documentation/release-notes.md#write-for-the-users-impact) | Medium |
| Are entries grouped by kind? | [group entries by kind](../../../authoring/documentation/release-notes.md#group-entries-by-kind) | Low |
| Are breaking changes first, with migration steps? | [call out breaking changes first](../../../authoring/documentation/release-notes.md#call-out-breaking-changes-first) | Medium |
| Does each deprecation name the replacement and removal timing? | [announce deprecations with a path](../../../authoring/documentation/release-notes.md#announce-deprecations-with-a-path) | Medium |
| Was the entry added with the change? | [write the entry in the same change](../../../authoring/documentation/release-notes.md#write-the-entry-in-the-same-change) | Medium |
| Are security fixes free of exploit details and private data? | [keep sensitive details out](../../../authoring/documentation/release-notes.md#keep-sensitive-details-out) | Low |

## Blocking

Blocking: an unannounced breaking change, and sensitive details. Others are optional.
