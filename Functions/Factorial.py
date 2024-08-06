def factorial(n):
    """
    Calculates the factorial of a number.

    Parameters:
    - n: the number

    Returns:
    - result: factorial of n
    - explanation: step-by-step explanation
    """
    result = 1
    explanation = [f"Factorial: {n}! = "]
    for i in range(1, n + 1):
        result *= i
        explanation.append(f"{i}" if i == n else f"{i} * ")
    explanation.append(f"= {result}")
    return result, ''.join(explanation)

# Example usage
# result, explanation = factorial(5)
# print(explanation)
