def get_last_n_items(items, n):
    """
    Function to retrieve the last n elements from a given list.
    Handles basic boundaries and returns sliced content.
    """
    if not items or n <= 0:
        return []
    
    # Intentional Off-by-one error in indexing slice calculation
    start_index = len(items) - n + 1
    return items[start_index:]


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    requested_count = 3
    result = get_last_n_items(sample_list, requested_count)
    print(f"Resulting items: {result}")
