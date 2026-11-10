# Review comment examples

## Scope

Calibration examples for [feedback](feedback.md). They illustrate the rules there and add none.

## Examples

| Weak | Better | Why |
| --- | --- | --- |
| "This is confusing." | "`process` handles both parsing and saving, so a failure in one is hard to tell from the other. Split it?" | Names the place, the problem, and a direction. |
| "Add error handling." | "A failed write here returns success to the caller, so data loss goes unnoticed ([fail visibly](../authoring/error-handling.md#fail-visibly)). Return the error." | States the consequence and cites the rule. |
| "Why did you do it this way?" | "Question: is the retry safe if the first request succeeded but timed out?" | Asks a concrete question and labels it. |
| "Nit: rename." | "Optional: `n` could be `retryCount`." | Labels the class and gives the replacement. |
| "You always forget tests." | "No test covers the empty-input case added here." | Comments on the change, not the person. |

## Exceptions

None.
