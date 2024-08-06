def magnitude(z):
    """
    Calculates the magnitude of a complex number.

    Parameters:
    - z: complex number

    Returns:
    - result: magnitude of z
    - explanation: step-by-step explanation
    """
    result = abs(z)
    explanation = f"Magnitude: |{z}| = {result}"
    return result, explanation

# Example usage
#result, explanation = magnitude(3 + 4j)
#print(explanation)
