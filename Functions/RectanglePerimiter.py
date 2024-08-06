def perimeter_rectangle(length, width):
    """
    Calculates the perimeter of a rectangle given its length and width.

    Parameters:
    - length: length of the rectangle
    - width: width of the rectangle

    Returns:
    - result: perimeter of the rectangle
    - explanation: step-by-step explanation
    """
    result = 2 * (length + width)
    explanation = f"Perimeter of Rectangle: 2 * ({length} + {width}) = {result}"
    return result, explanation

# Example usage
# result, explanation = perimeter_rectangle(5, 3)
# print(explanation)
