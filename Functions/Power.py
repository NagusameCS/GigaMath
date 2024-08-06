def power(base, exponent):
    """
    Calculates the power of a number.

    Parameters:
    - base: the base number
    - exponent: the exponent

    Returns:
    - result: base raised to the power of exponent
    - explanation: step-by-step explanation
    """
    result = base ** exponent
    explanation = f"Power: {base}^{exponent} = {result}"
    return result, explanation

# Example usage
# result, explanation = power(2, 3)
# print(explanation)
