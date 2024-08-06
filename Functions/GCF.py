def gcf(a, b):
    """
    Calculates the greatest common factor of two numbers.

    Parameters:
    - a: first number
    - b: second number

    Returns:
    - result: greatest common factor of a and b
    - explanation: step-by-step explanation
    """
    explanation = [f"Finding GCF of {a} and {b}: "]
    while b:
        explanation.append(f"gcf({a}, {b}) = gcf({b}, {a % b})\n")
        a, b = b, a % b
    explanation.append(f"GCF is {a}")
    return a, ''.join(explanation)

# Example usage
#result, explanation = gcf(48, 18)
#print(explanation)
