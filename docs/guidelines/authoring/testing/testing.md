# Testing

## Scope

Deciding what to test and how. For which kinds of tests a project needs, see [test-strategy](test-strategy.md). Applies to automated tests and to manual verification where automation is impractical.

## Guidelines

### Test observable behavior

Assert on what consumers can detect through the [contract](../../core/glossary.md), not on internal structure. Tests tied to implementation break on harmless refactors and hide real regressions.

### Cover regressions

A bug fix should include a test that fails without the fix. If that is impractical, state why and how it was verified.

### Match coverage to risk

Test more where failure costs more: contracts, security, data, and complex logic ([risk tiers](../../core/risk-tiers.md)). Trivial code does not need its own test; a coverage percentage is not the goal.

### Test at the lowest level that gives confidence

Verify each behavior at the cheapest [level](test-strategy.md#test-levels) that can fail for the reason you care about. Lower levels are faster, more precise, and more stable; higher levels prove that parts work together. Logic belongs in unit tests; wiring and boundaries in integration tests; only a few critical journeys in end-to-end tests.

### Test each boundary where it exists

Verify behavior that depends on a real collaborator (database, network, file system, another service, framework) with that collaborator or a faithful stand-in, because a mock cannot reveal a mismatch with the real thing. Verify contracts with other components at that boundary.

### Do not duplicate coverage across levels

Cover a behavior at one level, plus a thin check at the next level that the pieces connect. Repeating the same assertions at every level multiplies cost and maintenance without adding confidence.

### Cover edge values and failures

Test edge values, empty and maximal inputs, invalid input, and failure paths, not only the happy path.

### Keep tests deterministic

A test must give the same result every run. Control time, randomness, ordering, and external services. A flaky test must be fixed or removed, not retried until green.

### Keep tests independent

Each test sets up its own state and does not depend on another test's order or leftovers.

### Make failures diagnosable

A failing test should say what was expected and what happened. One clear reason to fail per test.

### Never weaken a test to pass

Do not delete, loosen, or skip a test to make a change pass. If a test is wrong, fix it and say so. Changing expected behavior must be deliberate and explained.

## Examples

Observable behavior: for a sort function, assert the output order. Do not assert which internal algorithm ran.

## Exceptions

Throwaway or exploratory code needs no tests, but must not be shipped as is.
