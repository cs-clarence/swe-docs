# Checks: debugging and bug fixing

Verifies [authoring/debugging-and-bug-fixing](../../authoring/debugging-and-bug-fixing.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Was the failure reproduced before the fix, or is the lack of a reproduction stated? | [reproduce before fixing](../../authoring/debugging-and-bug-fixing.md#reproduce-before-fixing) | Medium |
| Does the fix address the cause rather than where the symptom appears? | [find the cause, not the symptom](../../authoring/debugging-and-bug-fixing.md#find-the-cause-not-the-symptom) | Medium |
| Was the cause isolated rather than guessed? | [change one thing at a time](../../authoring/debugging-and-bug-fixing.md#change-one-thing-at-a-time) | Low |
| Does a test fail without the fix and pass with it? | [cover the bug with a test](../../authoring/debugging-and-bug-fixing.md#cover-the-bug-with-a-test) | Medium |
| Were other places with the same pattern checked? | [look for the same defect elsewhere](../../authoring/debugging-and-bug-fixing.md#look-for-the-same-defect-elsewhere) | Medium |
| Are temporary debugging aids removed? | [remove debugging aids](../../authoring/debugging-and-bug-fixing.md#remove-debugging-aids) | Low |
| Is a non-obvious cause explained? | [explain a non-obvious cause](../../authoring/debugging-and-bug-fixing.md#explain-a-non-obvious-cause) | Low |

## Blocking

Blocking: a fix with no evidence the failure is gone, and a symptom patch that leaves the cause in place where it affects correctness or safety. Others are should fix.
