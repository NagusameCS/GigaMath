def prime_factors(n):
    """
    Finds the prime factors of a number.

    Parameters:
    - n: the number

    Returns:
    - result: list of prime factors of n
    - explanation: step-by-step explanation
    """
    factors = []
    explanation = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            explanation.append(f"{n} / {d} = ")
            n //= d
            explanation.append(f"{n}\n")
        d += 1
    return factors, ''.join(explanation)

# Example usage
# result, explanation = prime_factors(56)
# print(explanation)
