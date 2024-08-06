def fibonacci(n):
    """
    Generates the first n Fibonacci numbers.

    Parameters:
    - n: number of Fibonacci numbers to generate

    Returns:
    - result: list of first n Fibonacci numbers
    - explanation: step-by-step explanation
    """
    result = [0, 1]
    explanation = ["Fibonacci sequence:\n0\n1\n"]
    for i in range(2, n):
        result.append(result[-1] + result[-2])
        explanation.append(f"{result[-1]}\n")
    return result[:n], ''.join(explanation)

# Example usage
# result, explanation = fibonacci(10)
# print(explanation)
