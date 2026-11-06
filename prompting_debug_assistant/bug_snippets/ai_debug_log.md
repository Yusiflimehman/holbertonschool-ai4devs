## Bug 1 – bug1.py
**AI Diagnosis**: The slice `items[len(items) - n + 1:]` skips the first intended element, resulting in an off-by-one error.  
**Suggested Fix**: Change the slicing expression to `items[len(items) - n:]` or use negative indexing `items[-n:]`.  
**Alternative Fixes Tested**: Negative slicing `items[-n:]`.  
**Result**: Fix works as expected.

## Bug 2 – bug2.js
**AI Diagnosis**: The loop condition `i <= prices.length` causes an out-of-bounds error, and `price[i]` references an undefined variable instead of `prices[i]`.  
**Suggested Fix**: Change loop condition to `i < prices.length` and fix variable name to `prices[i]`.  
**Alternative Fixes Tested**: Array.prototype.reduce method `prices.reduce((acc, curr) => acc + curr, 0)`.  
**Result**: Fix works as expected.

## Bug 3 – bug3.py
**AI Diagnosis**: Performing division by zero throws an unhandled `ZeroDivisionError` exception during execution.  
**Suggested Fix**: Handle zero division using a `try-except ZeroDivisionError` block or check `b != 0` before operation.  
**Alternative Fixes Tested**: Conditional input check before division.  
**Result**: Fix works as expected.

## Bug 4 – bug4.js
**AI Diagnosis**: Using single equality assignment operator `=` inside `if (age = 18)` mutates `age` to 18 and always returns true.  
**Suggested Fix**: Replace assignment `=` with comparison operator `===` or `>=`.  
**Alternative Fixes Tested**: Relational comparison `age >= 18`.  
**Result**: Fix works as expected.

## Bug 5 – bug5.cpp
**AI Diagnosis**: Accessing index `10` on a vector with only 5 elements leads to out-of-bounds memory access and undefined behavior.  
**Suggested Fix**: Bound-check the index before accessing, or use `numbers.at(10)` to safely catch `std::out_of_range`.  
**Alternative Fixes Tested**: Bounds checking using `numbers.size()`.  
**Result**: Fix works as expected.
