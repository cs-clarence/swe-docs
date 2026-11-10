# Review by tier

## Scope

A quick map from a change's [risk tier](../core/risk-tiers.md) to the checks to run. It adds no checks.

## How to use

Run every row in the matching [checks](checks) files whose tier is at or below the change's tier. A change in tier Low runs Low rows only; Medium runs Low and Medium; High runs all.

## Checks per file

| File | Low | Medium | High |
| --- | --- | --- | --- |
| [abstraction](checks/structure/abstraction.md) | 3 | 8 | 0 |
| [accessibility-and-i18n](checks/ui/accessibility-and-i18n.md) | 1 | 4 | 0 |
| [agents](checks/planning/agents.md) | 1 | 7 | 1 |
| [approach](checks/approach.md) | 6 | 2 | 0 |
| [architecture](checks/structure/architecture.md) | 0 | 10 | 3 |
| [authentication-and-sessions](checks/security/authentication-and-sessions.md) | 0 | 2 | 8 |
| [break-down-work](checks/planning/break-down-work.md) | 0 | 6 | 1 |
| [change-size](checks/planning/change-size.md) | 1 | 5 | 0 |
| [choose-the-approach](checks/planning/approaches/choose-the-approach.md) | 1 | 5 | 0 |
| [comments](checks/comments.md) | 5 | 2 | 0 |
| [concurrency](checks/concurrency.md) | 0 | 3 | 3 |
| [configuration](checks/configuration.md) | 3 | 3 | 0 |
| [cryptography](checks/security/cryptography.md) | 0 | 3 | 8 |
| [data-and-state](checks/database/data-and-state.md) | 0 | 2 | 4 |
| [data-retention-and-deletion](checks/security/data-retention-and-deletion.md) | 0 | 3 | 5 |
| [database-and-queries](checks/database/database-and-queries.md) | 0 | 4 | 5 |
| [database-keys](checks/database/database-keys.md) | 0 | 4 | 1 |
| [debugging-and-bug-fixing](checks/debugging-and-bug-fixing.md) | 3 | 4 | 0 |
| [dependencies](checks/dependencies.md) | 2 | 3 | 0 |
| [design](checks/structure/design.md) | 0 | 4 | 1 |
| [documentation](checks/documentation.md) | 4 | 2 | 0 |
| [error-handling](checks/error-handling.md) | 1 | 8 | 1 |
| [flaky-tests](checks/testing/flaky-tests.md) | 2 | 5 | 1 |
| [generated-and-vendored-code](checks/generated-and-vendored-code.md) | 2 | 6 | 0 |
| [identifiers-and-keys](checks/identifiers-and-keys.md) | 0 | 7 | 2 |
| [input-handling](checks/security/input-handling.md) | 1 | 6 | 4 |
| [interfaces-and-compatibility](checks/interfaces-and-compatibility.md) | 1 | 4 | 2 |
| [large-changes](checks/planning/large-changes.md) | 0 | 3 | 4 |
| [large-work](checks/planning/approaches/large-work.md) | 0 | 3 | 5 |
| [medium-work](checks/planning/approaches/medium-work.md) | 0 | 7 | 0 |
| [modularity](checks/structure/modularity.md) | 1 | 9 | 1 |
| [new-project](checks/planning/approaches/new-project.md) | 1 | 6 | 2 |
| [observability](checks/observability.md) | 2 | 3 | 0 |
| [output-handling](checks/security/output-handling.md) | 1 | 3 | 1 |
| [performance](checks/performance.md) | 1 | 5 | 0 |
| [plan-a-change](checks/planning/plan-a-change.md) | 0 | 6 | 3 |
| [refactoring](checks/structure/refactoring.md) | 3 | 3 | 0 |
| [releases-and-rollback](checks/releases-and-rollback.md) | 1 | 4 | 4 |
| [resilience](checks/resilience.md) | 0 | 4 | 2 |
| [security-and-privacy](checks/security/security-and-privacy.md) | 2 | 4 | 4 |
| [self-review](checks/self-review.md) | 3 | 3 | 0 |
| [small-work](checks/planning/approaches/small-work.md) | 3 | 2 | 0 |
| [style](checks/style.md) | 7 | 0 | 0 |
| [test-doubles-and-data](checks/testing/test-doubles-and-data.md) | 1 | 7 | 1 |
| [test-strategy](checks/testing/test-strategy.md) | 1 | 5 | 0 |
| [testing](checks/testing/testing.md) | 2 | 9 | 0 |
| [threat-review](checks/threat-review.md) | 0 | 2 | 9 |
| [time-and-numbers](checks/time-and-numbers.md) | 0 | 4 | 2 |
| [ui-behavior](checks/ui/ui-behavior.md) | 0 | 8 | 1 |