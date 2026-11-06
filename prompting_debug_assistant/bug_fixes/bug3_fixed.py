def divide_user_inputs(a, b):
    """
    Fixed function with proper zero division handling.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    res1 = divide_user_inputs(10, 2)
    res2 = divide_user_inputs(10, 0)
    print("Test Output 1:", res1)
    print("Test Output 2:", res2)
    assert res1 == 5.0, f"Expected 5.0, got {res1}"
    assert res2 == "Cannot divide by zero", f"Expected error string, got {res2}"
