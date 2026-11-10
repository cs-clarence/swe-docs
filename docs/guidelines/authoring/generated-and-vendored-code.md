# Generated and vendored code

## Scope

Code produced by tools and code copied in from elsewhere. Third-party packages are in [dependencies](dependencies.md).

## Guidelines

### Do not edit generated code by hand

Change the source or the generator and regenerate. A hand edit is lost on the next run.

### Mark generated files

Put a header saying the file is generated, from what, and how to regenerate it.

### Make generation reproducible

Pin the generator and its inputs ([pin versions reproducibly](dependencies.md#pin-versions-reproducibly)) so the same inputs give the same output.

### State whether generated output is committed

Commit it when consumers need it without the generator, and otherwise build it. Say which. Mixed practice causes stale files.

### Review the source of generation

Review the specification, template, or generator input, and skim the output for surprises. Reading thousands of generated lines finds little.

### Keep vendored code unmodified

Copy it as is. If a patch is needed, keep it separate, with a reason and the upstream version, so it can be reapplied.

### Record the origin of vendored code

Note the source, version, and license ([vet before adding](dependencies.md#vet-before-adding)).

### Update vendored code deliberately

Treat an update as adding a dependency, including its review, and keep security fixes current.

## Exceptions

Generated scaffolding that becomes hand-maintained should lose its generated marker. Say so.
