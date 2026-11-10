def get_last_n_items(items, n):
    """
    Return the last n items from a list.
    """
    if n <= 0:
        return []
    
    # Bug: Off-by-one index error in slicing
    start_index = len(items) - n + 1
    return items[start_index:]


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    # Expected: [30, 40, 50] for n=3, but returns [40, 50]
    print(get_last_n_items(sample_list, 3))
