def variance(data):
    """
    Calculates the variance of a list of numbers.

    Parameters:
    - data: list of numbers

    Returns:
    - result: variance of the numbers
    - explanation: step-by-step explanation
    """
    m = sum(data) / len(data)
    result = sum((x - m) ** 2 for x in data) / len(data)
    explanation = f"Variance: sum((x - {m})^2) / {len(data)} = {result}"
    return result, explanation

# Example usage
# result, explanation = variance([1, 2, 3, 4, 5])
# print(explanation)
