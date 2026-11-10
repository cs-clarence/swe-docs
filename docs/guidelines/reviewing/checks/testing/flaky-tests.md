# Checks: flaky tests

Verifies [authoring/flaky-tests](../../../authoring/testing/flaky-tests.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is a known flaky test being fixed, not tolerated? | [treat a flaky test as a defect](../../../authoring/testing/flaky-tests.md#treat-a-flaky-test-as-a-defect) | Medium |
| Are failures investigated rather than rerun until they pass? | [do not retry a test to make it pass](../../../authoring/testing/flaky-tests.md#do-not-retry-a-test-to-make-it-pass) | Medium |
| Were the usual causes of flakiness checked? | [look at the usual causes first](../../../authoring/testing/flaky-tests.md#look-at-the-usual-causes-first) | Low |
| Are time and randomness controlled in the test? | [control time and randomness](../../../authoring/testing/flaky-tests.md#control-time-and-randomness) | Medium |
| Do tests wait for conditions rather than fixed durations? | [wait for a condition, not a duration](../../../authoring/testing/flaky-tests.md#wait-for-a-condition-not-a-duration) | Medium |
| Is a quarantined test owned, dated, and its gap stated? | [quarantine with an owner and an end date](../../../authoring/testing/flaky-tests.md#quarantine-with-an-owner-and-an-end-date) | Medium |
| Does a failure leave enough evidence to reproduce it? | [capture evidence on failure](../../../authoring/testing/flaky-tests.md#capture-evidence-on-failure) | Low |
| Was a real race in the product ruled out? | [consider that the product may be flaky](../../../authoring/testing/flaky-tests.md#consider-that-the-product-may-be-flaky) | High |

## Blocking

Blocking: retrying or skipping a test to hide a real failure, and an unowned quarantine with no end date. Others are should fix.
