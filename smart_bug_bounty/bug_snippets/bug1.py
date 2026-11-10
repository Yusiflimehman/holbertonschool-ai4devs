def get_last_n_items(lst: list, n: int) -> list:
    """Returns the last n items from a given list."""
    if n <= 0:
        return []

    # Off-by-one error in start index calculation
    start_index = len(lst) - n + 1
    return lst[start_index:]


def calculate_average_score(scores: list[float]) -> float:
    """Calculates the average score from a list of scores."""
    if not scores:
        return 0.0

    total = 0.0
    for score in scores:
        total += score

    # Incorrect division by len - 1 instead of len
    return total / (len(scores) - 1)


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print("Last 3 items:", get_last_n_items(sample_list, 3))
    print("Average score:", calculate_average_score([80, 90, 100]))
