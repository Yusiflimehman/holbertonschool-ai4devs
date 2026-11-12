# Translation Guide - Log Analyzer

This guide records what we learned while translating the Python `LogAnalyzer` (the reference) into JavaScript and Go. All three versions return the same JSON output: `total_requests`, `unique_visitors`, `error_rate` and `status_counts`.

## Python → JavaScript

### Idiomatic differences
- `dict` → plain object: `status_counts["2xx"]` stays almost identical.
- `set()` → `new Set()`; `len(s)` → `s.size`.
- `None` → `null`.
- `re.compile(r"...")` → regular expression literal `/.../`; named groups change from `(?P<ip>...)` to `(?<ip>...)`.
- `str.strip()` → `trim()`, `str.isdigit()` → `/^\d+$/.test(...)`.
- Methods use camelCase (`parseLine`) instead of snake_case (`parse_line`), while the JSON keys stay snake_case so the output matches.

### Common pitfalls
- `Math.round` rounds exact ties up, but Python's `round()` rounds them to the even digit (`round(3.125, 2)` is `3.12`).
- `parseInt("12abc")` returns `12` instead of failing, so the input must be validated first.
- Splitting a file on `"\n"` leaves a `"\r"` on Windows files, so split on `/\r?\n/`.

## Python → Go

### Idiomatic differences
- `dict` → `struct` with JSON tags. Keys such as `"2xx"` are not valid Go names, so the tag `json:"2xx"` is used.
- `set` → `map[string]struct{}`.
- `None` → `nil`; a function that may return nothing returns a pointer (`*ParsedLine`).
- Exceptions → returned errors (`err`), checked right after the call.
- Dynamic typing → strict static typing; unused imports and variables are compile errors.
- Named regex groups work, but their values are collected manually with `SubexpNames()`.
- Everything is explicit: loops instead of comprehensions, `switch` instead of `if/elif`.

### Common pitfalls
- `int / int` is integer division in Go, so counts must be converted with `float64(...)` before dividing.
- `math.Round` rounds ties away from zero, which differs from Python. `strconv.FormatFloat(x, 'f', 2, 64)` rounds the exact value and sends ties to the even digit, like Python.
- Go's `map` is written to JSON with keys sorted alphabetically, so a `struct` keeps a predictable key order.
- A `package main` program cannot be imported from another folder, so the tests build it and run it as a command.
- `\d` matches only ASCII digits in Go and JavaScript, but Unicode digits in Python.

## Best Practices
1. Treat the reference implementation as the source of truth and translate its behavior, not only its syntax.
2. Keep one shared test file (`tests/test_cases.json`) and run it from every language.
3. Test edge cases: empty input, corrupted lines, redirects (3xx), and rounding ties such as 1 error in 32 requests (3.125%).
4. Compare outputs between languages on the same input, including a large generated file.
5. Keep the public names and output fields identical across languages.
6. Do not trust an automatic review blindly: when a reviewer claimed the Go rounding was wrong, a test with Python's expected values showed it was correct.
7. Measure performance after correctness is proven, and compare the implementations as written.
