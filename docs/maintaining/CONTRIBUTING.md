# Contributing to the Guidelines

For people editing `docs/guidelines/`. This folder is not shipped with the guidelines.

## Constraints on the guidelines

- **Workflow- and tool-neutral.** Say "change" and "reviewer", not PR, branch, commit, or ticket. Name no tools or languages in rules.
- **No repo-specific content.** Consumers cannot edit the folder; they override rules in their own files.
- **Relative links inside the folder only.** No absolute paths, no links out. It must work under any path.
- **Self-contained files.** Each states its scope.
- **Authoring holds rules; reviewing links to them.** Never restate a rule; link to its heading.
- **Core links to nothing above it. Authoring never links to reviewing** (except `authoring/README.md`).
- **Test for any rule:** would a reasonable team in another language and workflow object? If yes, it belongs in repo docs.

## Headings are public

Consumers reference rules by file and heading. Renaming or removing a heading, or tightening or loosening a rule, is a breaking change: record it in [CHANGELOG](../guidelines/CHANGELOG.md). Prefer adding rules to tightening. Update every link to a changed heading, including in `reviewing/checks/`.

## Every authoring topic has a matching checks file

Add `reviewing/checks/<topic>.md` when adding `authoring/<topic>.md`.

## Writing style: concise but lossless

Cut words, not information.

- Lead with the rule: one imperative sentence, reason in one clause.
- Keep qualifiers (when, unless, at least). A short rule without its condition is lossy.
- Remove filler, preamble, hedging, and restated rules. Never remove a distinction, threshold, or exception.
- Link instead of repeating.
- Use tables and bullets for parallel items; prose for reasoning.
- Include an example only where the rule is ambiguous without it; show the boundary.
- Prefer observable behavior over abstract qualities.
- Define each term once in `core/glossary.md`; use it consistently.
- Aim for about two pages per file; split if it covers two topics.
- Self-check: could any sentence be deleted without losing a rule, condition, or reason? Could a reader misapply a rule because something was cut?

## Normative language

Use must, should, may as defined in [glossary](../guidelines/core/glossary.md). Reserve must for real requirements.

## Templates

[guideline](templates/guideline.md) for authoring files, [review-check](templates/review-check.md) for checks files.
