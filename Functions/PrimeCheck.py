def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    - n: the number

    Returns:
    - result: True if n is prime, False otherwise
    - explanation: step-by-step explanation
    """
    if n <= 1:
        return False, f"{n} is not prime (<=1)"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False, f"{n} is not prime ({i} divides {n})"
    return True, f"{n} is prime"

# Example usage
# result, explanation = is_prime(7)
# print(explanation)
