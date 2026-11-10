# CI recipe

Run these on every change to `docs/`, from the repository root. Each exits non-zero on failure.

```sh
python3 docs/maintaining/scripts/validate_links.py
python3 docs/maintaining/scripts/lint_drafts.py
python3 docs/maintaining/scripts/by_tier.py   # then commit any change to reviewing/by-tier.md
python3 docs/maintaining/scripts/check_headings.py <previous release tag>
```

When tagging a release, also run `lint_drafts.py --release` so no draft ships under a stability promise, or move drafts out first. See [VERSIONING](VERSIONING.md).

The repository runs these in `.github/workflows/docs.yml` on every pull request and on pushes to `main`. `check_headings.py` runs on pull requests against the base branch. The `docs` job is the required check on `main`.
