def divide_numbers(a, b):
    """
    Divides two numbers and prints the execution log.
    Ensures input parameters are numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    print(f"Dividing {a} by {b}")
    # Bug: Missing zero division exception handling
    result = a / b
    print(f"Successfully calculated result: {result}")
    return result
