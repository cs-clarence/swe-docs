# Documentation

## Scope

External docs: READMEs, guides, references, and changelogs. Inline comments are in [comments](comments.md).

## Guidelines

### Write for a named reader

State who the document is for and what they can do after reading it. A document for everyone fits no one.

### Update docs in the same change as behavior

Change docs when behavior, interfaces, or setup change. Stale docs mislead more than missing docs.

### Link to facts instead of copying them

Describe a fact in one place and link to it ([keep one source of truth](structure/architecture.md#keep-one-source-of-truth)). Copies drift.

### Make examples runnable

Give examples that work as written, and verify them when feasible ([examples as tests](testing/test-strategy.md#cross-cutting-kinds)).

### Document the why and the limits

Explain purpose, constraints, and known limitations, not only steps. Code and tools already show the steps.

### Keep sensitive data out of docs

Do not put secrets or personal data in documentation or examples ([security-and-privacy](security/security-and-privacy.md#keep-sensitive-data-out-of-output)).

## Exceptions

Prototypes may defer docs; state that they are undocumented.
