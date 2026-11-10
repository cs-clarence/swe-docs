# Comments

## Scope

Inline comments, doc comments on code elements, and annotations such as TODOs. For external documentation (README, guides, setup), see the repository's docs. For naming and layout, see [style](style.md); for commented-out code, see [remove dead code](style.md#remove-dead-code).

## Guidelines

### Explain why, not what

A comment states intent, constraints, trade-offs, or non-obvious decisions. The code shows what it does. A comment that restates the code adds noise and goes stale.

### Fix the code before commenting it

If a comment exists to explain confusing code, first try a clearer name, a smaller unit, or a named constant ([style](style.md)). Comment what remains.

### Comment what the code cannot say

Always comment: workarounds (with the reason and when they can be removed), invariants and assumptions, units and formats, required ordering, performance or security reasons for an unusual choice, and intentionally ignored errors ([error-handling](error-handling.md#never-swallow-failures)).

### Document public contracts

Doc comments on public elements state purpose, inputs and outputs, errors, side effects, and guarantees ([contract](../core/glossary.md)), so callers need not read the implementation. Match the repository's doc-comment format.

### Keep comments accurate

When you change code, update or delete the comments about it. A wrong comment is worse than none.

### Give TODOs a handle

A TODO states what is left and why, and names an owner, tracker reference, or trigger condition. Do not leave unanchored TODOs, and do not use them to defer required work in the current change.

### Do not record history or credit

Do not note who changed what or when in comments; version history does that. Explain current behavior, not how it got here, unless the history explains a non-obvious constraint.

## Examples

| Avoid | Prefer |
| --- | --- |
| `// increment i` above `i++` | No comment. |
| `// loop through users` | A function name such as `activeUsers()`. |
| `// TODO: fix this` | `// TODO(billing): remove once v1 invoices are retired (tracked as BILL-123)` |
| `// retry` | `// Upstream drops the first request after idle; retry once.` |
| `// changed by Sam, 2020` | Nothing. |

## Exceptions

Generated and vendored code keeps its original comments. A required license or legal header may be kept as is.
