def get_last_n_items(items, n):
    # Intentional Off-by-one error
    return items[len(items) - n + 1:]

numbers = [10, 20, 30, 40, 50]
print(get_last_n_items(numbers, 2))
