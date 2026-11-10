# swe-docs

Reusable coding guidelines for authoring and reviewing changes, for humans and agents. The guidelines are in [docs/guidelines](docs/guidelines/README.md). Notes for maintainers are in [docs/maintaining](docs/maintaining/CONTRIBUTING.md) and are not part of what you install.

## Install

Both methods put the guidelines at `docs/guidelines` in your repository. Keep the folder structure and file names as they are, because the files link to each other by relative path.

### With omni

This repository has a projection manifest, [projection.omni.yaml](projection.omni.yaml). It links each area of `docs/guidelines` into your repository as a symlink.

Register this repository as a projection source in your [workspace configuration](https://github.com/omni-oss/json-schemas/blob/main/workspace.json), for example `workspace.omni.yaml`:

```yaml
projections:
  - source: git
    id: swe-docs
    uri: https://github.com/cs-clarence/swe-docs
    rev: main # pin a tag or commit to control when updates arrive
```

To install only some areas, set `routes` on the source to the areas you want. Reviewing links to authoring, and authoring links to core, so drop areas from the top down. See the [projection schema](https://github.com/omni-oss/json-schemas/blob/main/projection.json) for the fields.

By default, `omni ignore sync` adds every projection link to your ignore files. Set `ignore.sources.projections` to `false` in the workspace configuration if you want the links tracked.

### Manually

1. Copy or symlink `docs/guidelines` into your repository, for example to `docs/guidelines`.
2. To use only part of it, keep `README.md` and `core/`, then add `authoring/` and `reviewing/` as needed.
3. Treat the folder as read-only. To change a rule for your repository, write an [override](docs/guidelines/core/precedence.md#overriding-rules) in your own files.

A copy does not update by itself. Re-copy to get changes, and check the [changelog](docs/guidelines/CHANGELOG.md) for renamed headings that your overrides link to.

### Then

Add one line to your repository's instruction or contributor file, such as `AGENTS.md` or `CONTRIBUTING.md`: "Follow the guidelines in `docs/guidelines`."
