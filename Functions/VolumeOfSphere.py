def volume_sphere(radius):
    """
    Calculates the volume of a sphere given its radius.

    Parameters:
    - radius: radius of the sphere

    Returns:
    - result: volume of the sphere
    - explanation: step-by-step explanation
    """
    import math
    result = (4 / 3) * math.pi * radius ** 3
    explanation = f"Volume of Sphere: (4/3) * π * {radius}^3 = {result}"
    return result, explanation

# Example usage
# result, explanation = volume_sphere(3)
# print(explanation)
