# Fix Validation

## bug1.py
- Original Issue: Off-by-one error in the loop range — the last window was never averaged.
- Fix Applied: Changed `range(len(values) - window)` to `range(len(values) - window + 1)`.
- Test Results: All 3 test cases passed
  - `moving_average([10, 12, 14, 16, 18], 2)` → `[11.0, 13.0, 15.0, 17.0]` ✅
  - `moving_average([1, 2, 3], 3)` → `[2.0]` ✅
  - `moving_average([1, 2], 3)` → `[]` ✅

## bug2.js
- Original Issue: `forEach` did not wait for `async` callbacks, so an empty array was returned.
- Fix Applied: Replaced `forEach` with `await Promise.all(ids.map(...))` and mapped the results to names.
- Test Results: All 3 test cases passed
  - `getUserNames([1, 2, 3])` → `["User1", "User2", "User3"]` ✅
  - `getUserNames([])` → `[]` ✅
  - `getUserNames([7])` → `["User7"]` ✅

## bug3.java
- Original Issue: Strings were compared with `==` (reference equality) instead of value equality.
- Fix Applied: Changed `word == target` to `word.equals(target)`.
- Test Results: All 3 test cases passed
  - `["apple", "banana", "apple", "cherry", "apple"]`, target `new String("apple")` → `3` ✅
  - `["kiwi", "pear"]`, target `"apple"` → `0` ✅
  - empty list, target `"apple"` → `0` ✅

## bug4.cpp
- Original Issue: Loop condition `low < high` skipped the last remaining candidate, so first/last elements were not found.
- Fix Applied: Changed the loop condition to `low <= high`.
- Test Results: All 4 test cases passed
  - `{2, 5, 8, 12, 16, 23, 38}`, target `2` → `0` ✅
  - same array, target `38` → `6` ✅
  - same array, target `9` (missing) → `-1` ✅
  - `{7}`, target `7` → `0` ✅

## bug5.py
- Original Issue: Mutable default argument `tags=[]` was shared between all `Task` instances.
- Fix Applied: Changed the default to `tags=None` and create a new list in `__init__` (`list(tags) if tags is not None else []`).
- Test Results: All 3 test cases passed
  - Two tasks without tags → each keeps only its own tag (`['work']`, `['personal']`) ✅
  - Passing an existing list → original list is not modified ✅
  - Adding the same tag twice → stored only once ✅
