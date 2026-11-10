# Fix Validation

## bug1_fixed.py (fixes bug1.py)
- Original File: `bug_snippets/bug1.py`
- Fixed File: `bug_fixes/bug1_fixed.py`
- Original Issue: Off-by-one error in the loop range — the last window was never averaged.
- Fix Applied: Changed `range(len(values) - window)` to `range(len(values) - window + 1)`.
- Test Results: All 3 test cases passed
  - Test 1: `moving_average([10, 12, 14, 16, 18], 2)` → `[11.0, 13.0, 15.0, 17.0]` — PASS
  - Test 2: `moving_average([1, 2, 3], 3)` → `[2.0]` — PASS
  - Test 3: `moving_average([1, 2], 3)` → `[]` — PASS
- Status: PASS

## bug2_fixed.js (fixes bug2.js)
- Original File: `bug_snippets/bug2.js`
- Fixed File: `bug_fixes/bug2_fixed.js`
- Original Issue: `forEach` did not wait for `async` callbacks, so an empty array was returned.
- Fix Applied: Replaced `forEach` with `await Promise.all(ids.map(...))` and mapped the results to names.
- Test Results: All 3 test cases passed
  - Test 1: `getUserNames([1, 2, 3])` → `["User1", "User2", "User3"]` — PASS
  - Test 2: `getUserNames([])` → `[]` — PASS
  - Test 3: `getUserNames([7])` → `["User7"]` — PASS
- Status: PASS

## bug3_fixed.java (fixes bug3.java)
- Original File: `bug_snippets/bug3.java`
- Fixed File: `bug_fixes/bug3_fixed.java`
- Original Issue: Strings were compared with `==` (reference equality) instead of value equality.
- Fix Applied: Changed `word == target` to `word.equals(target)`.
- Test Results: All 3 test cases passed
  - Test 1: `["apple", "banana", "apple", "cherry", "apple"]`, target `new String("apple")` → `3` — PASS
  - Test 2: `["kiwi", "pear"]`, target `"apple"` → `0` — PASS
  - Test 3: empty list, target `"apple"` → `0` — PASS
- Status: PASS

## bug4_fixed.cpp (fixes bug4.cpp)
- Original File: `bug_snippets/bug4.cpp`
- Fixed File: `bug_fixes/bug4_fixed.cpp`
- Original Issue: Loop condition `low < high` skipped the last remaining candidate, so the first and last elements were not found.
- Fix Applied: Changed the loop condition from `low < high` to `low <= high`.
- Test Results: All 3 test cases passed
  - Test 1: `{2, 5, 8, 12, 16, 23, 38}`, target `2` → `0` — PASS
  - Test 2: `{2, 5, 8, 12, 16, 23, 38}`, target `38` → `6` — PASS
  - Test 3: `{2, 5, 8, 12, 16, 23, 38}`, target `9` (missing) → `-1` — PASS
- Status: PASS

## bug5_fixed.py (fixes bug5.py)
- Original File: `bug_snippets/bug5.py`
- Fixed File: `bug_fixes/bug5_fixed.py`
- Original Issue: Mutable default argument `tags=[]` was shared between all `Task` instances.
- Fix Applied: Changed the default to `tags=None` and create a new list in `__init__` (`list(tags) if tags is not None else []`).
- Test Results: All 3 test cases passed
  - Test 1: Two tasks without tags → each keeps only its own tag (`['work']`, `['personal']`) — PASS
  - Test 2: Passing an existing list → the original list is not modified — PASS
  - Test 3: Adding the same tag twice → stored only once — PASS
- Status: PASS

## Summary
| Original File | Fixed File | Tests Passed | Status |
|---|---|---|---|
| bug1.py | bug1_fixed.py | 3/3 | PASS |
| bug2.js | bug2_fixed.js | 3/3 | PASS |
| bug3.java | bug3_fixed.java | 3/3 | PASS |
| bug4.cpp | bug4_fixed.cpp | 3/3 | PASS |
| bug5.py | bug5_fixed.py | 3/3 | PASS |
