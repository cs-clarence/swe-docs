# Checks: test doubles and test data

Verifies [authoring/test-doubles-and-data](../../../authoring/testing/test-doubles-and-data.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Are real collaborators used where they are cheap and deterministic? | [prefer the real collaborator when it is cheap](../../../authoring/testing/test-doubles-and-data.md#prefer-the-real-collaborator-when-it-is-cheap) | Medium |
| Are fakes used for boundaries that cannot run in tests? | [use fakes for boundaries you cannot run](../../../authoring/testing/test-doubles-and-data.md#use-fakes-for-boundaries-you-cannot-run) | Medium |
| Is each fake verified against the real thing? | [check a fake against the real thing](../../../authoring/testing/test-doubles-and-data.md#check-a-fake-against-the-real-thing) | Medium |
| Are call assertions limited to cases where the call is the behavior? | [assert interactions only when they are the behavior](../../../authoring/testing/test-doubles-and-data.md#assert-interactions-only-when-they-are-the-behavior) | Medium |
| Are third-party APIs doubled through your own interface? | [wrap what you do not own before doubling it](../../../authoring/testing/test-doubles-and-data.md#wrap-what-you-do-not-own-before-doubling-it) | Medium |
| Does each test show the data values it depends on? | [state the values a test depends on](../../../authoring/testing/test-doubles-and-data.md#state-the-values-a-test-depends-on) | Low |
| Does test data include realistic and edge cases? | [use realistic data where it matters](../../../authoring/testing/test-doubles-and-data.md#use-realistic-data-where-it-matters) | Medium |
| Is mutable test data isolated per test? | [do not share mutable test data](../../../authoring/testing/test-doubles-and-data.md#do-not-share-mutable-test-data) | Medium |
| Is test data synthetic? | [use synthetic data](../../../authoring/testing/test-doubles-and-data.md#use-synthetic-data) | High |

## Blocking

Blocking: real personal data in test data, and fakes that no check keeps in line with the real system where the tier requires integration confidence. Others are should fix.
