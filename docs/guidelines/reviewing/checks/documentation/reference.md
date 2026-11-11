# Checks: reference

Verifies [authoring/documentation/reference](../../../authoring/documentation/reference.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does it describe without instructing? | [describe, do not instruct](../../../authoring/documentation/reference.md#describe-do-not-instruct) | Low |
| Does it follow the structure of the thing described? | [follow the structure of the thing described](../../../authoring/documentation/reference.md#follow-the-structure-of-the-thing-described) | Low |
| Does each entry give types, defaults, limits, and errors? | [state the facts a caller needs](../../../authoring/documentation/reference.md#state-the-facts-a-caller-needs) | Medium |
| Is every public entry covered in the same format? | [be complete and consistent](../../../authoring/documentation/reference.md#be-complete-and-consistent) | Medium |
| Is it generated from the source where possible? | [generate from the source where possible](../../../authoring/documentation/reference.md#generate-from-the-source-where-possible) | Medium |
| Where the interface is described in code (doc comments, help, API annotations), is that the reference and is it complete when surfaced? | [treat in-code descriptions as the user's reference](../../../authoring/documentation/reference.md#treat-in-code-descriptions-as-the-users-reference) | Medium |
| Are examples short and needed? | [keep examples short](../../../authoring/documentation/reference.md#keep-examples-short) | Low |

## Blocking

Blocking: reference that contradicts the behavior it describes. Others are optional.
