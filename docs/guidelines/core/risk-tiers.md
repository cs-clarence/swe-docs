# Risk tiers

## Scope

Authors use tiers to size verification; reviewers use them to size scrutiny.

## Tiers

| Tier | A change is this tier when it… | Examples |
| --- | --- | --- |
| **Low** | Cannot change behavior, or is easily caught and reversed. | Typos, comments, formatting, renames covered by the compiler or tests. |
| **Medium** | Changes behavior within one component; effects are contained. | New feature in one module, bug fix, refactor of internals. |
| **High** | Touches a contract, security or privacy, persistent data, or concurrency, or is hard to reverse. | Public API change, authentication, schema or data migration, shared state, deletion, deployment-affecting settings. |

## Rules

- When uncertain between two tiers, choose the higher.
- Take the highest tier that applies to any part of the change.
- A repository may add criteria for its domain (for example, anything touching payments is high) as an [override](precedence.md#overriding-rules).

## Effort by tier

| | Low | Medium | High |
| --- | --- | --- | --- |
| Author verification | Confirm it builds or reads correctly. | Test changed behavior and nearby failure paths. | Test thoroughly, including failure and rollback paths; state residual risk. |
| Review depth | Skim for mistakes and scope. | Check correctness, tests, and design for touched areas. | Check every applicable area; consider a second reviewer. |
| Description | One line. | What and why. | What, why, risks, alternatives, how to undo. |
