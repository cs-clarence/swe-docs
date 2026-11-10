# Input handling

## Scope

Receiving and checking data from outside a component. The basic rules are [validate at boundaries](../error-handling.md#validate-at-boundaries) and [treat external input as untrusted](security-and-privacy.md#treat-external-input-as-untrusted); this file adds how to apply them.

## Guidelines

### Parse input into validated types

Convert raw input once, at the boundary, into a type or structure that can only hold valid values ([make invalid states hard to represent](../structure/design.md#make-invalid-states-hard-to-represent)). Later code then cannot receive the unvalidated form.

### Check shape (syntactic) and meaning (semantic) separately

Validate syntax (type, range, format) at the boundary, and validate semantics, meaning the business rules (allowed, unique, permitted), where the rule lives. Each check then sits where its data is available.

### Enforce semantic rules where the data changes

Run semantic checks in the domain logic that makes the change, and enforce any rule that depends on stored state in the store itself, such as a uniqueness constraint ([enforce invariants where data lives](../database/data-and-state.md#enforce-invariants-where-data-lives)). A check made earlier can be stale by the time of the write, and other writers bypass application code.

### Accept known-good input

Allow what is defined as valid instead of blocking known-bad values. A denylist misses what you did not think of.

### Canonicalize before checking

Normalize encoding, case, paths, and separators first, then validate and use the normalized value. Otherwise the check and the use can see different values.

### Reject or sanitize, and say which

Either refuse invalid input or transform it by a stated rule. Do not silently repair it, because callers cannot know what you did.

### Keep data separate from commands

Pass input to queries, shells, templates, and paths as parameters or encoded values, never by concatenation ([treat external input as untrusted](security-and-privacy.md#treat-external-input-as-untrusted)).

### Enforce limits on size, depth, and rate

Cap length, nesting, count, and request rate before processing ([bound resource use](../performance.md#bound-resource-use)). Unbounded input is a denial-of-service path.

### Validate again at each trust boundary

Check at every boundary the data crosses, including between services. A check in a client or an outer layer does not replace one behind it.

### Return complete, safe errors for bad input

Report every invalid field at once, say what is wrong and how to fix it, and reveal no internals or sensitive data ([write useful messages](../error-handling.md#write-useful-messages)).

### Treat every external source as input

Apply these rules to files, messages from other systems, environment variables, command-line arguments, and output from tools or models, not only user-entered data.

## Examples

| | Syntactic validation | Semantic validation |
| --- | --- | --- |
| Question | Is it well formed? | Is it allowed, given the rules and current state? |
| Needs | The value alone. | Context: other data, stored state, the caller's identity. |
| Where | At the trust boundary, as the first step. | In domain logic, and in the store for state-dependent rules. |
| Failure | Reject early, with a field-level error. | Reject with a business-level error, at the point of the change. |
| Repeat at each boundary | Yes ([validate again](#validate-again-at-each-trust-boundary)). | Only where the rule is owned; do not copy rules between components. |

| Input | Handling |
| --- | --- |
| A date string in a request | Parse into a date type at the boundary. Check that it is not in the past where the booking rule lives. |
| An email field | Syntactic: it looks like an address, checked at the boundary. Semantic: it is not already registered, checked in the registration logic. |
| A file path from a user | Resolve to a canonical path, then check it is inside the allowed directory, then open it. |
| A search term used in a query | Pass it as a query parameter, never joined into the query text. |

## Exceptions

Trusted internal calls within one module need no repeated checks. Throwaway scripts may check less; state it.
