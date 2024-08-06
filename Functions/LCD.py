def lcm(a, b):
    """
    Calculates the least common multiple of two numbers.

    Parameters:
    - a: first number
    - b: second number

    Returns:
    - result: least common multiple of a and b
    - explanation: step-by-step explanation
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = abs(a * b) // gcd(a, b)
    explanation = f"LCM({a}, {b}) = |{a} * {b}| / GCD({a}, {b}) = {result}"
    return result, explanation

# Example usage
#result, explanation = lcm(12, 15)
#print(explanation)
