# Checks: authentication and sessions

Verifies [authoring/authentication-and-sessions](../../../authoring/security/authentication-and-sessions.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does every request needing identity require authentication by default? | [require authentication by default](../../../authoring/security/authentication-and-sessions.md#require-authentication-by-default) | High |
| Is authentication built on a vetted mechanism? | [use a vetted authentication mechanism](../../../authoring/security/authentication-and-sessions.md#use-a-vetted-authentication-mechanism) | High |
| Are credentials stored and handled as the cryptography rules require? | [store credentials safely](../../../authoring/security/authentication-and-sessions.md#store-credentials-safely) | High |
| Are session tokens from a secure source and long enough? | [make session tokens unguessable](../../../authoring/security/authentication-and-sessions.md#make-session-tokens-unguessable) | High |
| Can sessions expire and be revoked? | [expire and revoke sessions](../../../authoring/security/authentication-and-sessions.md#expire-and-revoke-sessions) | High |
| Is the session identifier replaced at login and on privilege change? | [issue a new session identifier on privilege change](../../../authoring/security/authentication-and-sessions.md#issue-a-new-session-identifier-on-privilege-change) | High |
| Are attempts limited without revealing which accounts exist? | [limit authentication attempts](../../../authoring/security/authentication-and-sessions.md#limit-authentication-attempts) | Medium |
| Are recovery flows as strong as login? | [protect recovery paths as strongly as login](../../../authoring/security/authentication-and-sessions.md#protect-recovery-paths-as-strongly-as-login) | High |
| Do sensitive actions require fresh or stronger proof? | [ask again for sensitive actions](../../../authoring/security/authentication-and-sessions.md#ask-again-for-sensitive-actions) | Medium |
| Is authorization still checked at the resource after authentication? | [keep authentication separate from authorization](../../../authoring/security/authentication-and-sessions.md#keep-authentication-separate-from-authorization) | High |

## Blocking

Blocking: unauthenticated access to protected operations, reversible or fast-hashed credentials, guessable tokens, and sessions that cannot be revoked. Others are should fix. Authentication changes are High risk.
