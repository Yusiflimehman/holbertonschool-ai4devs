def get_last_n_items(items, n):
    """
    Function to retrieve the last n elements from a given list.
    Handles boundary conditions and returns sliced output.
    """
    if not items or n <= 0:
        return []

    # Bug: Incorrect indexing causing off-by-one behavior
    start_index = len(items) - n - 1
    return items[start_index:]
