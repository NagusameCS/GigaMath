def log(x):
    """
    Calculates the natural logarithm of a value.

    Parameters:
    - x: the value

    Returns:
    - result: natural logarithm of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.log(x)
    explanation = f"Natural Logarithm: ln({x}) = {result}"
    return result, explanation

# Example usage
# result, explanation = log(math.e)
# print(explanation)
