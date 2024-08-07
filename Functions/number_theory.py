class NumberTheory:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False, f"{n} is not a prime number."
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False, f"{n} is not a prime number."
        return True, f"{n} is a prime number."

    @staticmethod
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        explanation = f"The prime factors of the number are {factors}."
        return factors, explanation

    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return [], "Fibonacci sequence is defined for positive integers."
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        explanation = f"The first {n} numbers in the Fibonacci sequence are {sequence}."
        return sequence, explanation
