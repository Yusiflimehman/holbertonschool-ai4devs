# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the moving average of every consecutive group of `window` values (e.g. `[10, 12, 14, 16, 18]` with window 2 → `[11.0, 13.0, 15.0, 17.0]`).
- **Current Issue**: Off-by-one error in the loop range — the last window is never computed, so the result is one element short (and an empty list is returned when `window == len(values)`).

## bug2.js
- **Intended Behavior**: Fetch every user by ID and return an array with all of their names (`["User1", "User2", "User3"]`).
- **Current Issue**: `forEach` does not wait for `async` callbacks, so the function returns the `names` array before any fetch finishes — the caller always gets an empty array.

## bug3.java
- **Intended Behavior**: Count how many times a target word appears in a list of words (`"apple"` → 3).
- **Current Issue**: Strings are compared with `==` (reference equality) instead of `.equals()` (value equality), so equal words created as different objects are never matched and the count is 0.

## bug4.cpp
- **Intended Behavior**: Binary search a sorted vector and return the index of the target, or `-1` if it is not present.
- **Current Issue**: The loop condition `low < high` stops before checking the case where `low == high`, so targets that end up as the last remaining candidate (e.g. the first or last element) are reported as not found.

## bug5.py
- **Intended Behavior**: Each `Task` object should have its own independent list of tags.
- **Current Issue**: A mutable default argument (`tags=[]`) is shared between all instances, so adding a tag to one task adds it to every task created without explicit tags.
