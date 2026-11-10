# Glossary

## Requirement levels

| Term | Meaning |
| --- | --- |
| **must** | Requirement. Deviate only with a stated reason and reviewer awareness; never silently. |
| **should** | Default. Deviate when there is a good reason; state it. |
| **may** | Optional. Use judgment. |

"Must not" and "should not" mirror the above.

A rule written as a plain imperative (for example, "Validate at boundaries") is a **must**. A rule that says *should* or *may* in its text carries that level instead.

## Terms

| Term | Meaning |
| --- | --- |
| **change** | Any modification proposed to a codebase, however delivered. |
| **author** | Whoever makes a change: human or agent. |
| **reviewer** | Whoever evaluates a change before it is accepted: human or agent. |
| **module** | A unit with a defined public interface: a package, library, namespace, or directory with an entry point. |
| **public interface** | What a module or component exposes for others to use; everything else is private. It is the module's [contract](#terms). |
| **contract** | What callers, users, or other systems may rely on: signatures, formats, behavior, guarantees. |
| **consumer** | Anything that depends on a contract. |
| **trust boundary** | A point where data or control passes between parties with different trust: user to system, service to service, system to storage, system to third party. |
| **observable behavior** | What a consumer can detect through the contract, as opposed to how it is implemented. |
| **baseline rule** | A rule as written in these guidelines. |
| **override** | A repository's recorded change to a baseline rule. See [precedence](precedence.md#overriding-rules). |
| **effective rule** | The baseline rule with any override applied. Authors and reviewers follow this. |
| **risk tier** | Low, medium, or high classification of a change. See [risk tiers](risk-tiers.md). |
