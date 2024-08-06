def phase(z):
    """
    Calculates the phase of a complex number.

    Parameters:
    - z: complex number

    Returns:
    - result: phase of z
    - explanation: step-by-step explanation
    """
    import math
    result = math.atan2(z.imag, z.real)
    explanation = f"Phase: phase({z}) = {result} radians"
    return result, explanation

# Example usage
#result, explanation = phase(1 + 1j)
#print(explanation)
