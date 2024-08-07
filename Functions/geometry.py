import math

class Geometry:
    @staticmethod
    def area_circle(radius):
        result = math.pi * (radius ** 2)
        explanation = f"The area of a circle with radius {radius} is {result}."
        return result, explanation

    @staticmethod
    def perimeter_rectangle(length, width):
        result = 2 * (length + width)
        explanation = f"The perimeter of a rectangle with length {length} and width {width} is {result}."
        return result, explanation

    @staticmethod
    def volume_sphere(radius):
        result = (4/3) * math.pi * (radius ** 3)
        explanation = f"The volume of a sphere with radius {radius} is {result}."
        return result, explanation
