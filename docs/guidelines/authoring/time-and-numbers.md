# Time and numbers

## Scope

Representing and computing with dates, times, durations, money, units, and numeric limits.

## Guidelines

### Store and exchange time in an unambiguous form

Use a single standard representation, such as UTC with an offset or zone, and convert only for display. Local times without a zone are ambiguous.

### Separate instants, durations, and calendar dates

Use the right type for each and do not add fixed seconds to mean "a day" or "a month". Days vary in length.

### Take the clock as a dependency

Pass the current time in, so code can be tested and made deterministic ([test through the interface](testing/testing.md)).

### Use exact types for money and counts

Use integers in the smallest unit or a decimal type for money. Binary floating point cannot represent most decimal fractions.

### Carry units and precision with values

Name or type values with their unit, and state rounding rules. Mixed units cause silent errors.

### Check ranges and overflow

Check limits of the numeric type for sizes, counts, and arithmetic on external input.

## Exceptions

Code that only displays a local time to a local user may keep local time; say so.
