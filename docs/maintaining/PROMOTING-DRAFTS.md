# Promoting drafts

A draft has a banner and a *(draft)* marker in the READMEs. It carries no stability promise.

Promote a draft when all of these hold:

1. A reviewer has read it against [CONTRIBUTING](CONTRIBUTING.md), and every rule passes the "would another team object?" test.
2. It was used on at least one real change, and the finding is in the [trial log](TRIAL-LOG.md).
3. Its `reviewing/checks/<topic>.md` exists, and each check links to a real heading.
4. It overlaps no existing rule, or links to the home of the shared rule.
5. `scripts/validate_links.py` and `scripts/lint_drafts.py` pass.

Then remove the banner and the *(draft)* markers, and add a [CHANGELOG](../guidelines/CHANGELOG.md) entry.
