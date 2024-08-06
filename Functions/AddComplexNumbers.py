def complex_add(a, b):
    """
    Adds two complex numbers.

    Parameters:
    - a: first complex number
    - b: second complex number

    Returns:
    - result: sum of a and b
    - explanation: step-by-step explanation
    """
    result = complex(a) + complex(b)
    explanation = f"Complex Addition: ({a}) + ({b}) = {result}"
    return result, explanation

# Example usage
result, explanation = complex_add(1 + 2j, 3 + 4j)
print(explanation)
