def atan(x):
    """
    Calculates the arctangent of a value.

    Parameters:
    - x: the value

    Returns:
    - result: arctangent of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.atan(x)
    explanation = f"Inverse Tangent: atan({x}) = {result} radians"
    return result, explanation

# Example usage
# result, explanation = atan(1)
# print(explanation)
