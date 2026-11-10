# Feedback

## Scope

Writing review comments and responding to them.

## Guidelines

### Be specific and actionable

Point to the exact place, state the problem and its consequence, and suggest a direction or fix when you know one. "Unclear" is not a finding; "this returns null on empty input, which the caller dereferences" is.

### Label the class

Mark each comment as blocking, should fix, optional, or question ([classes](process.md#classify-each-finding)) so the author knows what is required.

### Cite the rule or the evidence

Link the [rule](../authoring/README.md) or show the failing case. Findings without either are opinions; label them optional.

### Comment on the change, not the person

Describe the code and its effects. Keep tone neutral and factual.

### Ask when unsure

If you may be missing context, ask a question rather than asserting a defect.

### Acknowledge what is good when it is notable

Name good approaches worth repeating, briefly. Do not pad.

### Respond to every finding

Authors fix, decline with a reason, or ask. Do not leave findings silently unaddressed.

## Examples

| Weak | Strong |
| --- | --- |
| "This is confusing." | "Optional: `process()` handles both parsing and saving; splitting them would make the save path testable." |
| "Wrong." | "Blocking: input is concatenated into the query at line 40 ([validate input](../authoring/security/security-and-privacy.md#treat-external-input-as-untrusted)). Use a parameterized query." |
