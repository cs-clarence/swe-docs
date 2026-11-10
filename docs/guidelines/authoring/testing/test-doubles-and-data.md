# Test doubles and test data

## Scope

Stand-ins for collaborators, and the data tests run on. When to test at which level is in [testing](testing.md).

## Guidelines

### Prefer the real collaborator when it is cheap

Use the real one if it is fast, deterministic, and isolated. A double can only be as right as its author's guess.

### Use fakes for boundaries you cannot run

Use a small working implementation of a slow or external system instead of a script of expected calls.

### Check a fake against the real thing

Run the same tests against the fake and the real collaborator, or periodically verify it ([test each boundary where it exists](testing.md#test-each-boundary-where-it-exists)). Unchecked fakes drift.

### Assert interactions only when they are the behavior

Verify calls to a collaborator only when the call is the result, such as sending a notification. Otherwise it couples the test to how the code works ([test observable behavior](testing.md#test-observable-behavior)).

### Wrap what you do not own before doubling it

Put a library or service behind your own interface and double that ([isolate behind your own interface](../dependencies.md#isolate-behind-your-own-interface)). Doubling a third-party API ties tests to its details.

### State the values a test depends on

Build test data with builders or helpers whose defaults hide irrelevant fields and whose calls show the relevant ones. The reader should see what matters.

### Use realistic data where it matters

Include representative sizes, shapes, and [edge values](testing.md#cover-edge-values-and-failures). Tidy sample data hides the cases that break.

### Do not share mutable test data

Create or reset data for each test ([keep tests independent](testing.md#keep-tests-independent)).

### Use synthetic data

Do not copy real personal or sensitive data into tests ([minimize sensitive data](../security/security-and-privacy.md#minimize-sensitive-data)).

## Exceptions

Tests of a double itself may need to inspect its calls.
