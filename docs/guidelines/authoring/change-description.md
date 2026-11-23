# Change description

## Scope

What the written description of a change contains so a reviewer can judge it without asking. It adds the design section for wide changes and ties together rules stated elsewhere. It excludes release notes for users ([release-notes](documentation/release-notes.md)).

## Guidelines

### Lead with a summary a reviewer can act on

Open with what changed and why, in a few sentences, so a reviewer knows the purpose and the kind of review needed before reading the change. Link the request, issue, or plan instead of copying it.

### Report verification, risk, and how to undo

Include how the change was verified and what was not ([explain the result](approach.md#explain-the-result)), backed by evidence ([confirm each claim with evidence](self-review.md#confirm-each-claim-with-evidence)), and where you are least sure ([mark the riskiest part](self-review.md#mark-the-riskiest-part)). At High risk, also say how to undo the change.

### List alternatives at Medium risk and above

Name the alternatives rejected for each significant choice, and why. Where decisions are recorded is in [record significant decisions](structure/architecture.md#record-significant-decisions).

### Add a design section when the change reaches wide

Add a separate section, after the summary and clearly marked as optional reading, when the change has a wide blast radius, spans several components or systems, or alters architecture, a contract, or data flow. It tells the reviewer where to look beyond the diff, so reviewers of narrow changes can skip it.

The section covers:

- **Shape.** How the parts fit: the components touched, how they interact, and what moved or was added.
- **Blast radius.** What else can be affected: callers, consumers, data, deployments, other systems.
- **Where to look.** Pointers to the specific files, functions, or snippets that carry the design, each with a line on why it matters. Quote a snippet only when the diff does not show it clearly, such as a contract or a call path across files.
- **Review order.** Which pointers to read first when order matters.
- **Out of scope.** What you deliberately left unchanged that a reviewer might expect to change.

Keep it to what a reviewer needs to review the design. Do not retell the diff, and do not restate what the code makes obvious ([link to facts instead of copying them](documentation/documentation.md#link-to-facts-instead-of-copying-them)). Link a design document or decision record instead of repeating it.

### Match detail to the tier

Detail follows the Description row of [effort by tier](../core/risk-tiers.md#effort-by-tier). At High risk, add the design section when it applies.

## Examples

Design section for a change that moves session storage to a shared service:

| Weak | Better |
| --- | --- |
| "Refactored sessions across the codebase. See the diff." | "Session reads now go through the session service instead of each module's own store. Affects login, API gateway, and the admin tool. Start at `session/service` (the new contract) and the call in `gateway/auth` (the only path that can reject a request). Existing sessions are not migrated; see Out of scope." |

## Exceptions

A change that is Low risk and touches one place needs only the summary. An urgent fix may start with a short description; complete it afterwards and say what was skipped ([approach](approach.md#explain-the-result)).
