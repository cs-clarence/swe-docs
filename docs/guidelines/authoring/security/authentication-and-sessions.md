# Authentication and sessions

## Scope

Proving who a caller is and keeping that proof alive. What a caller may do is in [security-and-privacy](security-and-privacy.md).

## Guidelines

### Require authentication by default

Deny requests that need an identity unless authentication succeeded ([default to secure and closed](security-and-privacy.md#default-to-secure-and-closed)). Making each endpoint opt in leaves forgotten ones open.

### Use a vetted authentication mechanism

Use an established protocol and library ([use vetted libraries and protocols](security-and-privacy.md#use-vetted-libraries-and-protocols)). Custom login flows repeat known mistakes.

### Store credentials safely

Store passwords as [slow, salted hashes](cryptography.md#hash-passwords-with-a-slow-salted-function), and never log or return them.

### Make session tokens unguessable

Create tokens from a [secure random source](cryptography.md#generate-randomness-from-a-secure-source) with enough length that guessing is impractical.

### Expire and revoke sessions

Give sessions a maximum lifetime and an idle timeout, and end them on logout, password change, and loss of privilege. A session that cannot be ended outlives the reason it was granted.

### Issue a new session identifier on privilege change

Replace the identifier at login and when privilege changes. Reusing one lets an attacker who knew the old value keep access.

### Limit authentication attempts

Rate-limit or delay repeated attempts, and do not reveal whether an account exists. Unlimited attempts allow guessing at scale.

### Protect recovery paths as strongly as login

Make reset and recovery flows use single-use, time-limited tokens sent only to a verified channel. Attackers use the weakest path.

### Ask again for sensitive actions

Require recent proof of identity, or a stronger factor, before actions such as changing credentials or moving money.

### Keep authentication separate from authorization

Treat "who is this" and "may they do this" as separate checks, and make the second at the resource ([enforce authorization at the resource](security-and-privacy.md#enforce-authorization-at-the-resource)).

## Exceptions

A tool behind a gateway that already authenticates may rely on it. State which component authenticates.
