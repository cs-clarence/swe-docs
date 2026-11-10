# Checks: input handling

Verifies [authoring/input-handling](../../../authoring/security/input-handling.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is raw input converted once into a validated type at the boundary? | [parse input into validated types](../../../authoring/security/input-handling.md#parse-input-into-validated-types) | Medium |
| Are syntactic and semantic checks done in the right places? | [check shape (syntactic) and meaning (semantic) separately](../../../authoring/security/input-handling.md#check-shape-syntactic-and-meaning-semantic-separately) | Medium |
| Are state-dependent rules enforced where the data changes, including in the store? | [enforce semantic rules where the data changes](../../../authoring/security/input-handling.md#enforce-semantic-rules-where-the-data-changes) | High |
| Does validation allow known-good values rather than block known-bad ones? | [accept known-good input](../../../authoring/security/input-handling.md#accept-known-good-input) | Medium |
| Is input normalized before it is checked and used? | [canonicalize before checking](../../../authoring/security/input-handling.md#canonicalize-before-checking) | High |
| Is it clear whether invalid input is rejected or sanitized? | [reject or sanitize, and say which](../../../authoring/security/input-handling.md#reject-or-sanitize-and-say-which) | Medium |
| Is input kept separate from commands, queries, templates, and paths? | [keep data separate from commands](../../../authoring/security/input-handling.md#keep-data-separate-from-commands) | High |
| Are size, depth, and rate limited? | [enforce limits on size, depth, and rate](../../../authoring/security/input-handling.md#enforce-limits-on-size-depth-and-rate) | Medium |
| Is data checked again at each trust boundary? | [validate again at each trust boundary](../../../authoring/security/input-handling.md#validate-again-at-each-trust-boundary) | High |
| Do errors list all problems and leak nothing? | [return complete, safe errors for bad input](../../../authoring/security/input-handling.md#return-complete-safe-errors-for-bad-input) | Low |
| Are files, messages, environment, arguments, and tool output treated as input? | [treat every external source as input](../../../authoring/security/input-handling.md#treat-every-external-source-as-input) | Medium |

## Blocking

Blocking: input concatenated into commands or queries, missing checks at a trust boundary, unbounded input, and sensitive data in errors. Others are should fix.
