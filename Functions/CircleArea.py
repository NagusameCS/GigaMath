def area_circle(radius):
    """
    Calculates the area of a circle given its radius.

    Parameters:
    - radius: radius of the circle

    Returns:
    - result: area of the circle
    - explanation: step-by-step explanation
    """
    import math
    result = math.pi * radius ** 2
    explanation = f"Area of Circle: π * {radius}^2 = {result}"
    return result, explanation

# Example usage
# result, explanation = area_circle(5)
# print(explanation)
