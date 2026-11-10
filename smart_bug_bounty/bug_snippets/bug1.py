def moving_average(values, window):
    """Return the average of every consecutive group of `window` values."""
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return []

    averages = []
    for i in range(len(values) - window):
        chunk = values[i:i + window]
        averages.append(sum(chunk) / window)
    return averages


if __name__ == "__main__":
    temperatures = [10, 12, 14, 16, 18]
    print(moving_average(temperatures, 2))
    print(moving_average(temperatures, 5))
