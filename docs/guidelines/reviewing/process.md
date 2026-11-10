# Review process

## Scope

Any evaluation of a change by a human or agent.

## Guidelines

### Determine the risk tier

Classify the change using [risk tiers](../core/risk-tiers.md) and set depth accordingly. Re-tier upward if you find something riskier.

### Apply the effective rules

Check against baseline rules plus the repository's [overrides](../core/precedence.md#overriding-rules). Skip checks for disabled rules.

### Review in priority order

1. Purpose: does it do what was intended, and only that?
2. Correctness: does it behave properly, including edge and failure cases?
3. Security and privacy, data, and contracts: is anything unsafe or breaking?
4. Design: do structure and boundaries hold up?
5. Tests: do they verify the behavior and would they catch regressions?
6. Readability and style: can others maintain it?

Spend time on higher items first. Do not let style comments displace correctness findings.

### Use the checks for touched areas only

Apply the [checks](checks) for areas the change touches, at the depth the tier warrants. Do not run every checklist on every change.

### Review what the change actually does

Read the code, not only the description. Confirm that evidence supports claims about verification.

### Classify each finding

| Class | Meaning | Effect |
| --- | --- | --- |
| **Blocking** | Incorrect, unsafe, breaks a contract, violates a *must*, or lacks verification the tier requires. | Must be resolved or explicitly accepted by the owner before acceptance. |
| **Should fix** | Violates a *should* without a stated reason, or a meaningful maintainability problem. | Fix, or reply with a reason. |
| **Optional** | Preference, minor improvement, or follow-up. | Author's call. |
| **Question** | Reviewer lacks context. | Answer; may become another class. |

### Do not block on preference

If the repository's rules do not require it and it is not a correctness, safety, or maintainability problem, it is optional.

### Resolve disagreement on the merits

Decide disagreements by the rules, evidence, and the [precedence order](../core/precedence.md), not by seniority. Escalate to the task owner if still unresolved.

## Responsibilities

**Author:** make the change reviewable (small, scoped, explained, verified), state risks and assumptions, respond to every finding.

**Reviewer:** be timely, specific, and correct; say what was not reviewed; do not approve what you did not examine.

## Exceptions

For urgent changes, a shortened review is acceptable. State what was skipped so follow-up can happen.
