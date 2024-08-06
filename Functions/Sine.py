def sin(x):
    """
    Calculates the sine of an angle in radians.

    Parameters:
    - x: angle in radians

    Returns:
    - result: sine of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.sin(x)
    explanation = f"Sine: sin({x}) = {result}"
    return result, explanation

# Example usage
#result, explanation = sin(math.pi / 2)
#print(explanation)