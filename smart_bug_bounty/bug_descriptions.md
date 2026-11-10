cat << 'EOF' > bug_descriptions.md
# Bug Descriptions

## bug1.py
- **Intended Behavior**: 
  1. `get_last_n_items`: Return the last `n` items from the list.
  2. `calculate_average_score`: Calculate the exact arithmetic mean by dividing the sum of scores by total element count (`len(scores)`).
- **Current Issue**: 
  1. `get_last_n_items` has an off-by-one slicing index (`len(lst) - n + 1`), missing the first item of the requested range.
  2. `calculate_average_score` divides the total sum by `len(scores) - 1`, resulting in an incorrect, elevated average calculation.

## bug2.js
- **Intended Behavior**: 
  1. `fetchUserProfile`: Asynchronously wait for the user data to populate before returning it.
  2. `getActiveUsers`: Filter and return only users whose `isActive` property is `true` without modifying original object properties.
- **Current Issue**: 
  1. `fetchUserProfile` returns `userData` synchronously before `setTimeout` callback finishes, returning `null`.
  2. `getActiveUsers` uses assignment (`=`) instead of equality comparison (`===`), mutating all users' `isActive` property to `true` and including all users in the output.

## bug3.java
- **Intended Behavior**: 
  1. `removeShortStrings`: Safely iterate over and remove all strings shorter than `minLength` from the original list.
  2. `compareUserIds`: Correctly compare equality of value for two `Integer` objects.
- **Current Issue**: 
  1. `removeShortStrings` mutates the list while iterating forward, skipping elements adjacent to deleted ones.
  2. `compareUserIds` uses reference equality `==` instead of `.equals()`, failing when comparing `Integer` values outside the primitive caching range (-128 to 127).

## bug4.cpp
- **Intended Behavior**: 
  1. `createArray`: Dynamically allocate an array or fill a provided buffer, returning valid memory accessible in caller scope.
  2. `computeVectorMean`: Sum elements within valid vector bounds (from index `0` to `size - 1`).
- **Current Issue**: 
  1. `createArray` returns a dangling pointer to stack memory allocated in local scope (`tempArray`).
  2. `computeVectorMean` loop condition `i <= numbers.size()` causes an out-of-bounds array access (undefined behavior / segmentation fault).
EOF
