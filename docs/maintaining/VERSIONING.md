# Versioning

Consumers pin a release so updates arrive when they choose.

- Tag releases `vMAJOR.MINOR.PATCH`.
- **Major:** a heading was renamed or removed, or a rule was tightened or loosened. Each is listed in [CHANGELOG](../guidelines/CHANGELOG.md).
- **Minor:** a file or rule was added, or a draft was promoted.
- **Patch:** wording fixes that change no rule.
- Move the CHANGELOG "Unreleased" entries under the new tag when tagging.
- Run `scripts/validate_links.py` and `scripts/check_headings.py <previous tag>` before tagging.
- Drafts are not covered by the stability promise. Promote a draft by removing its draft marker and listing it in the CHANGELOG.
