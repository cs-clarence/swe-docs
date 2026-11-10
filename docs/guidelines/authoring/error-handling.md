# Error handling

## Scope

Input validation, failure behavior, error messages, cleanup, and retries.

## Guidelines

### Validate at boundaries

Check external input where it enters, for presence, type, range, and format. Code behind the boundary may then rely on validity.

### Fail visibly

When an operation cannot do what it promises, report it to the caller or operator. Do not return a plausible but wrong result.

### Never swallow failures

Do not catch an error and ignore it. Handle it, or propagate it. If you intentionally ignore one, say why in a comment.

### Handle errors at the right level

Handle an error where there is enough context to act on it; otherwise propagate it. Do not catch broadly to hide unknown problems.

### Preserve context

Keep the cause when wrapping or rethrowing, and add what was being attempted. Losing the original error makes diagnosis guesswork.

### Write useful messages

An error says what failed, with what input or state, and ideally what to do. Do not include secrets or sensitive data ([security-and-privacy](security/security-and-privacy.md#keep-sensitive-data-out-of-output)).

### Distinguish expected from unexpected

Expected failures (invalid input, not found) get defined, handled responses. Unexpected ones (bugs, broken invariants) must be reported prominently, not hidden.

### Clean up on every path

Release resources, locks, and temporary state on success, failure, and cancellation.

### Retry only what is safe and bounded

Retry only transient failures of operations that are safe to repeat, with a limit and increasing delay. Never retry unbounded or non-repeatable operations blindly.

### Define partial-failure behavior

When a multi-step operation can fail midway, decide and document whether it rolls back, continues, or leaves a recoverable state. Do not leave inconsistent state silently.

## Examples

| Avoid | Prefer |
| --- | --- |
| `catch { }` | Handle, propagate, or comment why it is safe to ignore. |
| `"Error"` | `"Cannot save profile 42: storage unavailable"` |
| Returning an empty list on a failed fetch | Reporting the failure; empty must mean empty. |

## Exceptions

Best-effort operations (such as optional telemetry) may drop failures. Do so explicitly and make sure dropping cannot affect correctness.
