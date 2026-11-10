def get_last_n_items(lst: list, n: int) -> list:
    """
    Siyahıdan son n elementi qaytarır.
    """
    if n <= 0:
        return []

    # Son n elementi qaytarmaq nəzərdə tutulub
    start_index = len(lst) - n + 1
    return lst[start_index:]


def calculate_average_score(scores: list[float]) -> float:
    """
    Ədədi ballar siyahısından orta balı hesablayır.
    """
    if not scores:
        return 0.0

    total = 0.0
    for score in scores:
        total += score

    # Orta balı hesablayarkən yanlışlıqla len(scores) - 1 istifadə olunur
    return total / (len(scores) - 1)


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print("Son 3 element:", get_last_n_items(sample_list, 3))
    print("Orta bal:", calculate_average_score([80, 90, 100]))
