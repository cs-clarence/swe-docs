# Authoring

Rules for writing and changing code. Start with [core principles](../core/principles.md). Scale effort with [risk tiers](../core/risk-tiers.md). Reviewers verify these rules using [reviewing](../reviewing/README.md).

| File | Covers |
| --- | --- |
| [approach](approach.md) | Understand, scope, implement, verify, explain. |
| [self-review](self-review.md) | What an author checks before asking for review. |
| [change-size](change-size.md) | How big a change should be and how to split it. |
| [debugging-and-bug-fixing](debugging-and-bug-fixing.md) | Reproduce, find the cause, test, look elsewhere. |
| [releases-and-rollback](releases-and-rollback.md) | Reversible, staged, observable releases. |
| [generated-and-vendored-code](generated-and-vendored-code.md) | Editing, marking, and updating generated and copied code. |
| [structure/](structure/README.md) | How code is divided and shaped. Files: architecture, modularity, abstraction, design, refactoring. |
| [ui/](ui/README.md) | How graphical interfaces behave and are made usable. Files: ui-behavior, accessibility-and-i18n. |
| [database/](database/README.md) | Stored data and how it is queried and changed. Files: data-and-state, database-and-queries, database-keys. |
| [testing/](testing/README.md) | Which tests to write and how to write them. Files: testing, test-strategy. |
| [security/](security/README.md) | Protecting data, boundaries, and secrets. Files: security-and-privacy, input-handling, output-handling, cryptography. |
| [error-handling](error-handling.md) | Validation, failure behavior, cleanup, retries. |
| [resilience](resilience.md) | Timeouts, retries, failing fast, degrading. |
| [concurrency](concurrency.md) | Shared state, timeouts, cancellation. |
| [observability](observability.md) | Logs, metrics, traces. |
| [performance](performance.md) | Measure, budget, bound. |
| [identifiers-and-keys](identifiers-and-keys.md) | Entity identifiers, cache and idempotency keys. |
| [time-and-numbers](time-and-numbers.md) | Time zones, durations, money, units, overflow. |
| [interfaces-and-compatibility](interfaces-and-compatibility.md) | Changing interfaces others depend on, including API design. |
| [configuration](configuration.md) | Settings, defaults, flags. |
| [dependencies](dependencies.md) | Adding, updating, removing dependencies. |
| [style](style.md) | Naming, readability, consistency. |
| [comments](comments.md) | Inline and doc comments, TODOs. |
| [documentation](documentation.md) | External docs. |
| [agents](agents.md) | Extra rules for agents. |

Before starting, check the repository's [overrides](../core/precedence.md#overriding-rules), if any. Each rule is a heading; the rule is the first sentence, followed by its reason and limits.
