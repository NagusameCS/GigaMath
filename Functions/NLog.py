def log10(x):
    """
    Calculates the logarithm base 10 of a value.

    Parameters:
    - x: the value

    Returns:
    - result: log base 10 of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.log10(x)
    explanation = f"Logarithm Base 10: log10({x}) = {result}"
    return result, explanation

# Example usage
# result, explanation = log10(100)
# print(explanation)
