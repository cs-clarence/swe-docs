# Coding guidelines

General guidelines for writing and reviewing code, for humans and agents. Language-, tool-, and workflow-neutral.

The aim is to work autonomously without going off the rails. Code is a means to an end, and it has to stay maintainable as the project grows. When the work turns out bigger than expected, or not as designed, [stop and ask](core/when-to-ask.md).

## Layout

| Area | Use it when |
| --- | --- |
| [core/](core/README.md) | Always. Shared principles, vocabulary, risk tiers, precedence. |
| [planning/](planning/README.md) | Deciding what to do and in what order, before building. |
| [authoring/](authoring/README.md) | Writing or changing code. Contains the rules. |
| [reviewing/](reviewing/README.md) | Evaluating a change. Checks that link back to the authoring rules. |

Links point one way: reviewing → authoring → planning → core. The usual order of use is planning, authoring, reviewing.

## Which files apply

| Task | Read |
| --- | --- |
| Choosing an approach for a fix, feature, large change, or new project | [choose-the-approach](planning/approaches/choose-the-approach.md) |
| Planning a change or breaking down work | [plan-a-change](planning/plan-a-change.md), [break-down-work](planning/break-down-work.md) |
| Reviewing a plan | [plan-a-change checks](reviewing/checks/planning/plan-a-change.md), [break-down-work checks](reviewing/checks/planning/break-down-work.md) |
| Work turned out bigger than expected or not as designed | [when-to-ask](core/when-to-ask.md) |
| Any change | [principles](core/principles.md), [approach](authoring/approach.md) |
| Finding and fixing a defect | [debugging-and-bug-fixing](authoring/debugging-and-bug-fixing.md) |
| Shipping and undoing a change | [releases-and-rollback](authoring/releases-and-rollback.md) |
| Login, sessions, deleting data | [authentication-and-sessions](authoring/security/authentication-and-sessions.md), [data-retention-and-deletion](authoring/security/data-retention-and-deletion.md) |
| Test doubles, test data, unreliable tests | [test-doubles-and-data](authoring/testing/test-doubles-and-data.md), [flaky-tests](authoring/testing/flaky-tests.md) |
| Migrating or replacing a large piece | [large-changes](planning/large-changes.md) |
| Generated or copied-in code | [generated-and-vendored-code](authoring/generated-and-vendored-code.md) |
| Knowing when a change is done | [core/definition-of-done](core/definition-of-done.md) |
| System or component structure | [architecture](authoring/structure/architecture.md) |
| Splitting, sizing, or merging modules | [modularity](authoring/structure/modularity.md) |
| Adding or changing an abstraction | [abstraction](authoring/structure/abstraction.md) |
| Structuring code inside a component | [design](authoring/structure/design.md) |
| Naming, layout | [style](authoring/style.md) |
| Writing or editing comments | [comments](authoring/comments.md) |
| Bug fix or new behavior | [approach](authoring/approach.md), [testing](authoring/testing/testing.md) |
| Deciding which tests a project needs | [test-strategy](authoring/testing/test-strategy.md) |
| Failure paths, validation | [error-handling](authoring/error-handling.md) |
| Input, auth, secrets, personal data | [security-and-privacy](authoring/security/security-and-privacy.md) |
| Parsing or validating external input | [input-handling](authoring/security/input-handling.md) |
| Encoding or returning data | [output-handling](authoring/security/output-handling.md) |
| Dates, times, money, units | [time-and-numbers](authoring/time-and-numbers.md) |
| Calling remote dependencies | [resilience](authoring/resilience.md) |
| Identifiers, cache and lookup keys | [identifiers-and-keys](authoring/identifiers-and-keys.md) |
| Primary and foreign keys | [database-keys](authoring/database/database-keys.md) |
| Encryption, hashing, signatures, tokens | [cryptography](authoring/security/cryptography.md) |
| Restructuring without behavior change | [refactoring](authoring/structure/refactoring.md) |
| Changing an API, format, or other published interface | [interfaces-and-compatibility](authoring/interfaces-and-compatibility.md) |
| Writing queries, indexes, transactions | [database-and-queries](authoring/database/database-and-queries.md) |
| Schemas, migrations, persistent data | [data-and-state](authoring/database/data-and-state.md) |
| Adding or updating a dependency | [dependencies](authoring/dependencies.md) |
| Speed or resource use | [performance](authoring/performance.md) |
| Logging, metrics, tracing | [observability](authoring/observability.md) |
| Threads, async work, shared state | [concurrency](authoring/concurrency.md) |
| Settings and feature flags | [configuration](authoring/configuration.md) |
| GUI states, feedback, error handling | [ui-behavior](authoring/ui/ui-behavior.md) |
| GUI accessibility and translation | [accessibility-and-i18n](authoring/ui/accessibility-and-i18n.md) |
| Any written document | [documentation](authoring/documentation/documentation.md) |
| Choosing what kind of document to write | [choosing-a-type](authoring/documentation/choosing-a-type.md) |
| User docs: tutorials, guides, reference, explanation, README, release notes | [documentation](authoring/documentation/README.md) |
| Developer docs kept with the code | [developer-docs](authoring/documentation/developer-docs.md) |
| Recording a significant decision | [decision-records](core/decision-records.md) |
| Agent planning work | [planning/agents](planning/agents.md) |
| Agent writing code | [authoring/agents](authoring/agents.md) |
| Reviewing a change | [reviewing/process](reviewing/process.md), then the matching [checks](reviewing/checks) |
| Self-reviewing before asking for review | [self-review](authoring/self-review.md) |
| Deciding how big a change should be | [change-size](planning/change-size.md) |
| Reviewing a high-risk security change | [threat-review](reviewing/checks/threat-review.md) |
| Reviewing agent output | [reviewing/agents](reviewing/agents.md) |

Scale effort to risk ([risk tiers](core/risk-tiers.md)). A small, low-risk change needs only the files it touches.

## Adopting

1. Make this folder available in the repo. A symlink works. The folder is self-contained and read-only for consumers.
2. Add one line to the repo's existing instruction or contributor file: "Follow the guidelines in `<path to this folder>`."

Nothing else is required. To change a rule for your repo, see [overriding rules](core/precedence.md#overriding-rules).

## Using subsets

Each file states its own scope. A repo may use only `core/` and `authoring/`, or drop files for areas it doesn't need. The indexes, including `core/README.md`, link to every area. In a subset install, delete the rows that point to omitted areas, or read the files directly.

See [CHANGELOG](CHANGELOG.md) for renamed or changed rules.
