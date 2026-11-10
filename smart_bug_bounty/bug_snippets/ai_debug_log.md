# AI Debug Log

**Prompt used for each snippet:**
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

## bug1.py
**AI Explanation**: The loop `range(len(values) - window)` stops one iteration too early, so the last window is never averaged. For 5 values and window 2 it returns 3 averages instead of 4, and it returns an empty list when `window == len(values)`.
**Suggested Fix**: Use `range(len(values) - window + 1)`.
**Confidence**: High

## bug2.js
**AI Explanation**: `Array.prototype.forEach` ignores the promises returned by `async` callbacks, so `getUserNames` returns the `names` array before any `fetchUser` call has resolved. The caller always receives an empty array.
**Suggested Fix**: Use `Promise.all` with `map`: `const users = await Promise.all(ids.map((id) => fetchUser(id))); return users.map((u) => u.name);` (or a `for...of` loop with `await`).
**Confidence**: High

## bug3.java
**AI Explanation**: `word == target` compares object references, not string contents. The words from `Scanner` and the `target` created with `new String("apple")` are different objects, so the comparison is always false and the count is 0.
**Suggested Fix**: Compare values with `word.equals(target)` (or `target.equals(word)`).
**Confidence**: High

## bug4.cpp
**AI Explanation**: The loop condition `while (low < high)` exits when `low == high` without checking that last remaining element. Targets that end up as the final candidate (such as the first element `2` or last element `38`) are reported as not found (`-1`).
**Suggested Fix**: Change the condition to `while (low <= high)`.
**Confidence**: High

## bug5.py
**AI Explanation**: The default argument `tags=[]` is evaluated once when the function is defined, so every `Task` created without explicit tags shares the same list object. Adding a tag to one task adds it to all of them.
**Suggested Fix**: Use `tags=None` and inside `__init__` write `self.tags = list(tags) if tags is not None else []`.
**Confidence**: High
