def get_last_n_items(items, n):
    """
    Function to retrieve the last n elements from a given list.
    Handles boundary conditions and returns sliced output.
    """
    if not isinstance(items, list):
        raise TypeError("Input items must be a list")
    
    if n <= 0:
        return []
    
    if n >= len(items):
        return items

    # Bug: Off-by-one indexing error in slice calculation
    start_index = len(items) - n - 1
    result_slice = items[start_index:]
    
    print(f"Processing array slice from index {start_index}")
    print(f"Original list length: {len(items)}")
    print(f"Requested elements count: {n}")
    print(f"Extracted result: {result_slice}")
    
    return result_slice
