# Debugging and bug fixing

## Scope

Finding and fixing a defect. The general activities are in [approach](approach.md).

## Guidelines

### Reproduce before fixing

Get a reliable reproduction first, or state that you could not. A fix without a reproduction cannot be shown to work.

### Find the cause, not the symptom

Trace to the first point where behavior differs from what is expected ([make the smallest sufficient change](approach.md#make-the-smallest-sufficient-change)). Patching where the symptom shows hides the defect.

### Change one thing at a time

Change one variable between runs, and bisect when the cause is unknown. Several simultaneous changes hide which one mattered.

### Cover the bug with a test

Add a test that fails before the fix and passes after ([cover regressions](testing/testing.md#cover-regressions)).

### Look for the same defect elsewhere

Search for other places that share the pattern, and fix them or report them. A defect from a shared habit or helper rarely occurs once.

### Remove debugging aids

Delete temporary logging, probes, and disabled checks before finishing, unless they earn a place under [observability](observability.md).

### Explain a non-obvious cause

State the cause and why it was missed when it is not obvious ([explain the result](approach.md#explain-the-result)), so the next reader does not repeat it.

## Exceptions

An urgent mitigation may come before the root cause. State that it is a stopgap, and follow up.
