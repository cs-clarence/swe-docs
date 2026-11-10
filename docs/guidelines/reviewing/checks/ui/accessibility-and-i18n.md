# Checks: accessibility and internationalization

Verifies [authoring/accessibility-and-i18n](../../../authoring/ui/accessibility-and-i18n.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is every function usable by keyboard and labeled for assistive tools? | [support non-pointer and assistive use](../../../authoring/ui/accessibility-and-i18n.md#support-non-pointer-and-assistive-use) | Medium |
| Is meaning conveyed by more than one cue? | [do not rely on one cue](../../../authoring/ui/accessibility-and-i18n.md#do-not-rely-on-one-cue) | Medium |
| Is user-visible text in resources? | [keep text out of code](../../../authoring/ui/accessibility-and-i18n.md#keep-text-out-of-code) | Low |
| Are dates, numbers, and layout locale-aware? | [handle locale differences](../../../authoring/ui/accessibility-and-i18n.md#handle-locale-differences) | Medium |
| Was it checked with assistive and non-default locale settings? | [test with real assistive and locale settings](../../../authoring/ui/accessibility-and-i18n.md#test-with-real-assistive-and-locale-settings) | Medium |

## Blocking

Blocking: functions unreachable without a pointer, where the audience requires access. Others are should fix.
