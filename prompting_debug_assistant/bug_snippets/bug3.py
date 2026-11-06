def divide_user_inputs(a, b):
    """
    Takes two numerical inputs and performs division operation.
    Intended to return quotient.
    """
    print(f"Attempting division of {a} by {b}...")
    
    # Intentional Runtime exception (ZeroDivisionError) without handling
    quotient = a / b
    
    return quotient


if __name__ == "__main__":
    num1 = 100
    num2 = 0
    calculated_value = divide_user_inputs(num1, num2)
    print("Final Division Result:", calculated_value)
