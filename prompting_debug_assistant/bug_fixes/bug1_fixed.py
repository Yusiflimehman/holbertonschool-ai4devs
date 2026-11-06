def get_last_n_items(items, n):
    """
    Fixed function to safely return the last n items from a list.
    """
    if not items or n <= 0:
        return []
    return items[-n:]


if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_n_items(sample_list, 3)
    print("Test Output:", result)
    assert result == [3, 4, 5], f"Expected [3, 4, 5], got {result}"
