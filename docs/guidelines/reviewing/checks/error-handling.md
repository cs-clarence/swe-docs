# Checks: error handling

Verifies [authoring/error-handling](../../authoring/error-handling.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is external input validated where it enters? | [validate at boundaries](../../authoring/error-handling.md#validate-at-boundaries) | Medium |
| Can an operation fail and still return a plausible result? | [fail visibly](../../authoring/error-handling.md#fail-visibly) | Medium |
| Is any caught error ignored without a stated reason? | [never swallow](../../authoring/error-handling.md#never-swallow-failures) | Low |
| Are errors handled where there is context, and catches narrow? | [right level](../../authoring/error-handling.md#handle-errors-at-the-right-level) | Medium |
| Is the original cause preserved when wrapping? | [preserve context](../../authoring/error-handling.md#preserve-context) | Medium |
| Do messages say what failed and avoid sensitive data? | [useful messages](../../authoring/error-handling.md#write-useful-messages) | Medium |
| Are resources released on success, failure, and cancellation? | [clean up](../../authoring/error-handling.md#clean-up-on-every-path) | Medium |
| Are retries limited to safe, repeatable operations, with a bound? | [retries](../../authoring/error-handling.md#retry-only-what-is-safe-and-bounded) | Medium |
| Is behavior defined when a multi-step operation fails midway? | [partial failure](../../authoring/error-handling.md#define-partial-failure-behavior) | High |
| Are expected failures handled and unexpected ones reported rather than hidden? | [distinguish expected from unexpected](../../authoring/error-handling.md#distinguish-expected-from-unexpected) | Medium |

## Blocking

Blocking: swallowed failures that can affect correctness, leaked resources, retries of non-repeatable operations that are not made safe, unbounded retries, and secrets in errors. Message wording is optional.
