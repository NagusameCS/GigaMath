def exp(x):
    """
    Calculates the exponential function e^x.

    Parameters:
    - x: the exponent

    Returns:
    - result: e raised to the power of x
    - explanation: step-by-step explanation
    """
    import math
    result = math.exp(x)
    explanation = f"Exponential: e^{x} = {result}"
    return result, explanation

# Example usage
#result, explanation = exp(1)
#print(explanation)
