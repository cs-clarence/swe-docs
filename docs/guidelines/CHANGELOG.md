# Changelog

Record renamed or removed headings, and rules made stricter or looser. Consumers link to rules by file and heading, so these changes can break overrides.

## Unreleased

- Initial guidelines: core, authoring (including architecture, modularity, abstraction, comments, test-strategy), reviewing, each with checks.
- core/glossary: plain imperative rules are *must*; added *module* and *public interface*.
- testing: renamed "Cover boundaries and failures" to "Cover edge values and failures"; removed "Report what is untested" (see approach: "Explain the result"); moved the where-to-test table to test-strategy.
- test-strategy: added kinds examples as tests, supported-environment, data-quality, validation or plan checks.
- modularity: removed "Do not reach into another module" (see architecture); "Keep dependencies one-way" became "Break dependency cycles"; removed the "Other situations" examples.
- comments: removed "Do not keep dead code in comments" (see style: "Remove dead code") and "Keep sensitive data out" (see security-and-privacy).
- agents: removed "Read local instructions first" and "Ask or state assumptions" (see approach).
- Plain-language pass: "public surface" is now "public interface" (modularity heading "Define the public interface first"; glossary term). security-and-privacy: "Use vetted primitives" is now "Use vetted libraries and protocols". Titles use sentence case.
- Added files: authoring (refactoring, documentation, interfaces-and-compatibility, data-and-state, dependencies, performance, observability, concurrency, configuration, accessibility-and-i18n, input-handling), core/decision-records, reviewing (by-tier, examples), and checks for each plus style.
- Added files: authoring (output-handling, time-and-numbers, resilience, identifiers-and-keys, cryptography) with checks.
- Restructured (breaking): closely related authoring files moved into group folders with a README each (structure, testing, security), and checks files mirror them under `reviewing/checks/<group>/`. Other files stay at the top level. Every moved path changed; headings did not. Update override paths, for example `authoring/testing.md` is now `authoring/testing/testing.md`.
- Added reviewing/checks/approach. Cross-linked idempotency keys between interfaces-and-compatibility and identifiers-and-keys.
- Restructured (breaking): `authoring/accessibility-and-i18n.md` moved to `authoring/ui/accessibility-and-i18n.md` and its checks to `reviewing/checks/ui/`. Headings did not change. Update override paths.
- Restructured (breaking): `authoring/data-and-state.md` moved to `authoring/database/data-and-state.md` and its checks to `reviewing/checks/database/`. Headings did not change. Update override paths.
- Moved (breaking): the "Database keys" section of `authoring/identifiers-and-keys.md` is now `authoring/database/database-keys.md`, with checks in `reviewing/checks/database/database-keys.md`. Its five rule headings are unchanged. Update override references to `identifiers-and-keys.md#give-each-table-or-collection-a-primary-key` and the other four.
- Promoted drafts: authoring (debugging-and-bug-fixing, releases-and-rollback, generated-and-vendored-code, change-size, self-review, ui/ui-behavior, database/database-and-queries, security/authentication-and-sessions, security/data-retention-and-deletion, testing/test-doubles-and-data, testing/flaky-tests, structure/large-changes), core/definition-of-done, and their checks including reviewing/checks/threat-review. They were promoted without a trial; expect rule edits.
- documentation: renamed "Keep one source of truth" to "Link to facts instead of copying them" and linked it to architecture: "Keep one source of truth", which stays the home of the rule.
