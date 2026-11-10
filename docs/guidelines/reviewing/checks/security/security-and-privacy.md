# Checks: security and privacy

Verifies [authoring/security-and-privacy](../../../authoring/security/security-and-privacy.md). Apply to any change touching input, identity, access, secrets, or sensitive data; these are usually [high tier](../../../core/risk-tiers.md).

| Check | Rule | Tier |
| --- | --- | --- |
| Are the trust boundaries this change crosses identified? | [trust boundaries](../../../authoring/security/security-and-privacy.md#identify-trust-boundaries) | High |
| Is external input validated and encoded for where it is used? | [untrusted input](../../../authoring/security/security-and-privacy.md#treat-external-input-as-untrusted) | Medium |
| Is authorization checked per action and resource, in the owning layer? | [authorization](../../../authoring/security/security-and-privacy.md#enforce-authorization-at-the-resource) | High |
| Does code and its access get only the privilege it needs? | [least privilege](../../../authoring/security/security-and-privacy.md#grant-least-privilege) | High |
| Are secrets absent from code, history, and fixtures? | [secrets](../../../authoring/security/security-and-privacy.md#keep-secrets-out-of-code-and-history) | Low |
| Is only necessary sensitive data collected and kept? | [minimize](../../../authoring/security/security-and-privacy.md#minimize-sensitive-data) | Medium |
| Do logs, errors, URLs, and analytics exclude sensitive data? | [output](../../../authoring/security/security-and-privacy.md#keep-sensitive-data-out-of-output) | Low |
| Do defaults and error paths deny rather than allow? | [secure defaults](../../../authoring/security/security-and-privacy.md#default-to-secure-and-closed) | Medium |
| Are cryptography and session handling done with vetted libraries? | [vetted libraries](../../../authoring/security/security-and-privacy.md#use-vetted-libraries-and-protocols) | Medium |
| Is security doubt stated and the change treated as high risk? | [surface security uncertainty](../../../authoring/security/security-and-privacy.md#surface-security-uncertainty) | High |

## Blocking

Everything above is blocking except where noted as optional by the repository. A security finding that cannot be assessed is a blocking question, not a pass.
