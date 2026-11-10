# Accessibility and internationalization

## Scope

Products with a graphical interface. Skip for products with none.

## Guidelines

### Support non-pointer and assistive use

Make every function reachable by keyboard and exposed to assistive technology with accurate labels and roles.

### Do not rely on one cue

Do not convey meaning by color, sound, or position alone.

### Keep text out of code

Put user-visible text in resources so it can be translated, and do not build sentences by concatenation.

### Handle locale differences

Use locale-aware formatting for dates, numbers, and sorting, and allow text to grow and change direction.

### Test with real assistive and locale settings

Check at least one screen reader or equivalent, and one non-default locale.

## Exceptions

Internal tools with a known, narrow audience may reduce scope; state it.
