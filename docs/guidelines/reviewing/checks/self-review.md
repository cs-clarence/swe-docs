# Checks: self-review

Verifies [authoring/self-review](../../authoring/self-review.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Was the whole change read from the start, as a reviewer would? | [read the change as a reviewer would](../../authoring/self-review.md#read-the-change-as-a-reviewer-would) | Low |
| Were the review checks for the touched areas applied, and findings fixed? | [run the checks for what you touched](../../authoring/self-review.md#run-the-checks-for-what-you-touched) | Medium |
| Are debugging aids, unrelated edits, and dead code removed? | [remove what does not belong](../../authoring/self-review.md#remove-what-does-not-belong) | Low |
| Does each claim in the description have evidence? | [confirm each claim with evidence](../../authoring/self-review.md#confirm-each-claim-with-evidence) | Medium |
| Does the description say where the author is least sure and what is unverified? | [mark the riskiest part](../../authoring/self-review.md#mark-the-riskiest-part) | Medium |
| Was a change with several purposes split? | [split what is too big](../../authoring/self-review.md#split-what-is-too-big) | Low |

## Blocking

A change with no sign of self-review, such as leftover debugging aids or claims with no evidence, goes back to the author. Others are should fix. Finding classes are in [process](../process.md#classify-each-finding).
