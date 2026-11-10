def get_last_n_items(items, n):
    """
    Intended: Return the last n items in a list.
    Fix: Use Python slice items[-n:] to get exact last n elements.
    """
    if n <= 0:
        return []
    return items[-n:]


def calculate_average(numbers):
    """
    Intended: Calculate average of non-negative numbers.
    Fix: Return 0.0 when count is 0 to avoid ZeroDivisionError.
    """
    total = 0
    count = 0
    for num in numbers:
        if num >= 0:
            total += num
            count += 1
    
    if count == 0:
        return 0.0
    return total / count


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print("Last 3 items:", get_last_n_items(sample_list, 3))
    print("Average:", calculate_average([-5, -10]))
