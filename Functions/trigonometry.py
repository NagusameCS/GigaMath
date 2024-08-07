import math

class Trigonometry:
    @staticmethod
    def sin(angle):
        result = math.sin(math.radians(angle))
        explanation = f"The sine of {angle} degrees is {result}."
        return result, explanation

    @staticmethod
    def cos(angle):
        result = math.cos(math.radians(angle))
        explanation = f"The cosine of {angle} degrees is {result}."
        return result, explanation

    @staticmethod
    def tan(angle):
        result = math.tan(math.radians(angle))
        explanation = f"The tangent of {angle} degrees is {result}."
        return result, explanation

    @staticmethod
    def asin(value):
        result = math.degrees(math.asin(value))
        explanation = f"The arc sine of {value} is {result} degrees."
        return result, explanation

    @staticmethod
    def acos(value):
        result = math.degrees(math.acos(value))
        explanation = f"The arc cosine of {value} is {result} degrees."
        return result, explanation

    @staticmethod
    def atan(value):
        result = math.degrees(math.atan(value))
        explanation = f"The arc tangent of {value} is {result} degrees."
        return result, explanation
