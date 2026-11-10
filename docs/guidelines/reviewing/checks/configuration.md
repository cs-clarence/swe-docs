# Checks: configuration

Verifies [authoring/configuration](../../authoring/configuration.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Are environment-specific values outside the code? | [keep configuration out of code](../../authoring/configuration.md#keep-configuration-out-of-code) | Low |
| Are defaults safe? | [choose safe defaults](../../authoring/configuration.md#choose-safe-defaults) | Medium |
| Is configuration validated at startup? | [validate at startup](../../authoring/configuration.md#validate-at-startup) | Medium |
| Are secrets kept apart from ordinary configuration? | [keep secrets separate](../../authoring/configuration.md#keep-secrets-separate) | Medium |
| Does each flag have an owner and removal point? | [give flags an owner and an end](../../authoring/configuration.md#give-flags-an-owner-and-an-end) | Low |
| Is each setting documented? | [document each setting](../../authoring/configuration.md#document-each-setting) | Low |

## Blocking

Blocking: unsafe defaults and secrets in configuration. Others are should fix.
