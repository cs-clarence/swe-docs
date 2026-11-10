# Checks: time and numbers

Verifies [authoring/time-and-numbers](../../authoring/time-and-numbers.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is time stored with an unambiguous zone or offset? | [store and exchange time in an unambiguous form](../../authoring/time-and-numbers.md#store-and-exchange-time-in-an-unambiguous-form) | High |
| Are instants, durations, and calendar dates distinct? | [separate instants, durations, and calendar dates](../../authoring/time-and-numbers.md#separate-instants-durations-and-calendar-dates) | Medium |
| Is the clock injected rather than read inline? | [take the clock as a dependency](../../authoring/time-and-numbers.md#take-the-clock-as-a-dependency) | Medium |
| Is money held in an exact type? | [use exact types for money and counts](../../authoring/time-and-numbers.md#use-exact-types-for-money-and-counts) | High |
| Are units and rounding explicit? | [carry units and precision with values](../../authoring/time-and-numbers.md#carry-units-and-precision-with-values) | Medium |
| Are overflow and range limits checked? | [check ranges and overflow](../../authoring/time-and-numbers.md#check-ranges-and-overflow) | Medium |

## Blocking

Blocking: floating-point money, ambiguous stored times, and unchecked overflow on external input. Others are should fix.
