## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The indexing fails to correctly slice the array when n equals list length.

## Bug 2 – bug2.js
**Intended Behavior**: Calculate the sum of all price elements in an array.  
**Issue Type**: Syntax and reference error.  
**Notes**: Loop goes out of bounds and accesses undefined variable 'price'.

## Bug 3 – bug3.py
**Intended Behavior**: Safely divide two numbers provided by the user.  
**Issue Type**: Runtime exception.  
**Notes**: Throws ZeroDivisionError when b is zero without handling.

## Bug 4 – bug4.js
**Intended Behavior**: Check if the user is 18 years old or older.  
**Issue Type**: Logical error.  
**Notes**: Uses assignment operator `=` instead of strict comparison `===`.

## Bug 5 – bug5.cpp
**Intended Behavior**: Print a specific element from a vector.  
**Issue Type**: Out of bounds memory access.  
**Notes**: Accesses index 5 on a vector of size 3.
