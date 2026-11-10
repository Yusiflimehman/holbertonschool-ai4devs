# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last `n` items from a given list.
- **Current Issue**: Off-by-one slicing error (`len(items) - n + 1`) which skips one item and returns fewer elements than requested.

## bug2.js
- **Intended Behavior**: Calculate the total price of items in a cart and apply a percentage discount.
- **Current Issue**: Out-of-bounds loop constraint (`i <= cartItems.length`) causes `NaN` errors when reading `undefined`, and discount calculation fails to divide the percentage by 100.

## bug3.java
- **Intended Behavior**: Compare user input password with stored password string and return `true` if they match.
- **Current Issue**: Uses reference comparison (`==`) instead of value equality (`.equals()`), causing valid password strings in different memory locations to evaluate as `false`.

## bug4.py
- **Intended Behavior**: Asynchronously fetch and aggregate user data for a list of user IDs.
- **Current Issue**: Invokes an asynchronous coroutine inside a standard synchronous loop without using `await` or an event loop, resulting in a list of raw coroutine objects instead of resolved user data.
