def std_dev(data):
    """
    Calculates the standard deviation of a list of numbers.

    Parameters:
    - data: list of numbers

    Returns:
    - result: standard deviation of the numbers
    - explanation: step-by-step explanation
    """
    m = sum(data) / len(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    result = variance ** 0.5
    explanation = f"Standard Deviation: sqrt(sum((x - {m})^2) / {len(data)}) = {result}"
    return result, explanation

# Example usage
#result, explanation = std_dev([1, 2, 3, 4, 5])
#print(explanation)
