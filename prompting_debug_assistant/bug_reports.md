## Bug Report – bug1.py
- **Summary**: Off-by-one error when attempting to slice the list elements.
- **Root Cause**: Subtracted an extra index in `items[len(items) - n + 1:]`, causing incorrect list slicing.
- **Resolution**: Changed to `items[-n:]` based on AI suggestion, which handles list slicing cleanly and avoids boundary issues.
- **Lesson Learned**: Always test edge cases with minimal input and prefer native negative indexing in Python over manual arithmetic.

## Bug Report – bug2.js
- **Summary**: Out-of-bounds loop and undefined variable reference.
- **Root Cause**: Used `i <= prices.length` which went past array boundaries, alongside calling undefined variable `price[i]`.
- **Resolution**: Updated loop boundary to `i < prices.length` and corrected variable reference to `prices[i]`.
- **Lesson Learned**: Carefully check loop exit conditions and verify array pluralization naming conventions.

## Bug Report – bug3.py
- **Summary**: Unhandled ZeroDivisionError exception during execution.
- **Root Cause**: Direct division operator `a / b` was called without validating if divisor `b` equals zero.
- **Resolution**: Implemented conditional validation `if b == 0:` to safely catch zero divisors before division.
- **Lesson Learned**: Always validate user inputs or wrap arithmetic operations in appropriate try-except blocks.

## Bug Report – bug4.js
- **Summary**: Logical error causing the age validation check to always pass.
- **Root Cause**: Used single assignment operator `=` (`if (age = 18)`) instead of relational comparison operator `>=`.
- **Resolution**: Changed assignment operator to relational comparison `age >= 18`.
- **Lesson Learned**: Be vigilant with equality operators in JavaScript conditions to prevent accidental variable re-assignments.

## Bug Report – bug5.cpp
- **Summary**: Out-of-bounds array access causing undefined memory behavior.
- **Root Cause**: Accessing index `10` on a std::vector instantiated with only 5 elements.
- **Resolution**: Added explicit bounds checking (`targetIndex < numbers.size()`) before attempting array element access.
- **Lesson Learned**: Always perform explicit vector size verification or use boundary-checked methods like `.at()` in C++.
