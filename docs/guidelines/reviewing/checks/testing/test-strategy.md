# Checks: test strategy

Verifies [authoring/test-strategy](../../../authoring/testing/test-strategy.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does new behavior have unit and integration tests, colocated where the repository allows? | [start with unit and integration](../../../authoring/testing/test-strategy.md#start-with-unit-and-integration-tests) | Medium |
| Are internal modules tested through their public interface like libraries, with application-level tests limited to composition? | [modules as libraries](../../../authoring/testing/test-strategy.md#test-internal-modules-as-libraries) | Medium |
| Is each extra kind of test justified by the product, interface, or a risk? | [extra kinds](../../../authoring/testing/test-strategy.md#choose-extra-kinds-by-product-and-interface) | Medium |
| Do the top-level tests use the interface real users or callers use? | [real interface](../../../authoring/testing/test-strategy.md#test-through-the-interface-users-actually-use) | Medium |
| Are high-level tests few and limited to critical paths? | [thin top](../../../authoring/testing/test-strategy.md#keep-the-top-thin) | Medium |
| Are tests named and classified by what they exercise, using the repository's names? | [naming](../../../authoring/testing/test-strategy.md#name-tests-by-what-they-exercise) | Low |

## Blocking

Blocking: no tests of the changed behavior at a level that can catch it (medium tier and above). Missing extra kinds are should fix unless the matrix marks them required for a high-tier change.
