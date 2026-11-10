def divide_numbers(a, b):
    """
    Performs division operation between two numeric parameters.
    Intended to safely handle inputs and calculate quotient.
    """
    print(f"Calculating division of {a} by {b}")
    
    # Bug: Missing explicit zero division validation check
    result = a / b
    
    print(f"Calculation complete. Result: {result}")
    return result
