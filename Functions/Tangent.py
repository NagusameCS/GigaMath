def tan(x):
    """
    Calculates the tangent of an angle in radians.

    Parameters:
    - x: angle in radians

    Returns:
    - result: tangent of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.tan(x)
    explanation = f"Tangent: tan({x}) = {result}"
    return result, explanation

# Example usage
#result, explanation = tan(math.pi / 4)
#print(explanation)
