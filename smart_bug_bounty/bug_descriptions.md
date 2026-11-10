# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items from a list and calculate average score.
- **Current Issue**: Off-by-one error in slicing index and incorrect division by len - 1 for average calculation.

## bug2.js
- **Intended Behavior**: Fetch user profile asynchronously and filter active users without modifying them.
- **Current Issue**: Synchronous return before timeout completes and assignment operator = used in if statement.

## bug3.java
- **Intended Behavior**: Remove short strings from a list and compare Integer objects.
- **Current Issue**: Mutates array during iteration skipping elements and uses reference equality == for Integers.

## bug4.cpp
- **Intended Behavior**: Allocate vector elements and compute mean score within vector boundaries.
- **Current Issue**: Returns stack memory pointer and has off-by-one out-of-bounds loop iteration condition.

## bug5.py
- **Intended Behavior**: Process items into independent cache and retry task up to max_attempts.
- **Current Issue**: Uses mutable default argument for dict cache and misses attempts counter increment.
