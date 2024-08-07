class Algebra:
    @staticmethod
    def add(a, b):
        result = a + b
        explanation = f"Adding {a} and {b} gives {result}."
        return result, explanation

    @staticmethod
    def subtract(a, b):
        result = a - b
        explanation = f"Subtracting {b} from {a} gives {result}."
        return result, explanation

    @staticmethod
    def multiply(a, b):
        result = a * b
        explanation = f"Multiplying {a} and {b} gives {result}."
        return result, explanation

    @staticmethod
    def divide(a, b):
        if b == 0:
            return None, "Cannot divide by zero."
        result = a / b
        explanation = f"Dividing {a} by {b} gives {result}."
        return result, explanation

    @staticmethod
    def power(a, b):
        result = a ** b
        explanation = f"Raising {a} to the power of {b} gives {result}."
        return result, explanation

    @staticmethod
    def sqrt(a):
        if a < 0:
            return None, "Cannot take the square root of a negative number."
        result = a ** 0.5
        explanation = f"The square root of {a} is {result}."
        return result, explanation

    @staticmethod
    def factorial(n):
        if n < 0:
            return None, "Cannot take the factorial of a negative number."
        if n == 0 or n == 1:
            return 1, "The factorial of 0 or 1 is 1."
        result = 1
        for i in range(2, n + 1):
            result *= i
        explanation = f"The factorial of {n} is {result}."
        return result, explanation

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        explanation = f"The greatest common divisor is {a}."
        return a, explanation

    @staticmethod
    def lcm(a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        result = abs(a * b) // gcd(a, b)
        explanation = f"The least common multiple of {a} and {b} is {result}."
        return result, explanation
