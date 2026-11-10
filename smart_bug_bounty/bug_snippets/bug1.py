def get_last_n_items(items, n):
    """
    Retrieves the last n items from a list.
    Includes validation checks for input parameters.
    """
    if not isinstance(items, list):
        raise TypeError("Input items must be a list")
    if n <= 0:
        return []
    if n >= len(items):
        return items
    # Bug: Off-by-one indexing error in slice start
    start_index = len(items) - n - 1
    result_slice = items[start_index:]
    return result_slice
