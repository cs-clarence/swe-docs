# Checks: testing

Verifies [authoring/testing](../../../authoring/testing/testing.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is each behavior verified at the lowest level that can catch it? | [lowest level](../../../authoring/testing/testing.md#test-at-the-lowest-level-that-gives-confidence) | Medium |
| Are real-collaborator behaviors verified against the real thing or a faithful stand-in, not only mocks? | [each boundary](../../../authoring/testing/testing.md#test-each-boundary-where-it-exists) | Medium |
| Are the same assertions repeated across levels? | [no duplicate coverage](../../../authoring/testing/testing.md#do-not-duplicate-coverage-across-levels) | Medium |
| Do tests assert observable behavior rather than internals? | [observable behavior](../../../authoring/testing/testing.md#test-observable-behavior) | Medium |
| Would the new test fail without the fix? | [regressions](../../../authoring/testing/testing.md#cover-regressions) | Medium |
| Is coverage heavier where failure costs more? | [match to risk](../../../authoring/testing/testing.md#match-coverage-to-risk) | Medium |
| Are edge values, invalid input, and failure paths covered? | [edge values and failures](../../../authoring/testing/testing.md#cover-edge-values-and-failures) | Medium |
| Could any test fail intermittently (time, order, randomness, network)? | [deterministic](../../../authoring/testing/testing.md#keep-tests-deterministic) | Medium |
| Does any test depend on another's state or order? | [independent](../../../authoring/testing/testing.md#keep-tests-independent) | Medium |
| Were any tests deleted, skipped, or loosened, and is that justified? | [never weaken](../../../authoring/testing/testing.md#never-weaken-a-test-to-pass) | Low |
| Does a failing test say what was expected and what happened? | [make failures diagnosable](../../../authoring/testing/testing.md#make-failures-diagnosable) | Low |

## Blocking

Blocking: no verification for a behavior change at medium or higher tier, weakened tests without justification, and flaky tests added. Missing edge-case tests in low-risk code are should fix.
