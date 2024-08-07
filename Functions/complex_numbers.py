import cmath

class ComplexNumbers:
    @staticmethod
    def complex_add(a, b):
        result = a + b
        explanation = f"Adding {a} and {b} gives {result}."
        return result, explanation

    @staticmethod
    def complex_multiply(a, b):
        result = a * b
        explanation = f"Multiplying {a} and {b} gives {result}."
        return result, explanation

    @staticmethod
    def magnitude(z):
        result = abs(z)
        explanation = f"The magnitude of {z} is {result}."
        return result, explanation

    @staticmethod
    def phase(z):
        result = cmath.phase(z)
        explanation = f"The phase angle of {z} is {result} radians."
        return result, explanation
