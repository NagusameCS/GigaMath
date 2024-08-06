import math

def solve_quadratic_equation(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0 for x.

    Parameters:
    - a: coefficient of x^2
    - b: coefficient of x
    - c: constant term

    Returns:
    - roots: tuple of solutions for x
    - explanation: step-by-step explanation of the solution process
    """
    explanation = []
    explanation.append(f"Starting with the equation: {a}x^2 + {b}x + {c} = 0")
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    explanation.append(f"Calculate the discriminant: D = {b}^2 - 4({a})({c}) = {discriminant}")
    
    if discriminant < 0:
        explanation.append("The discriminant is negative, so there are no real roots.")
        roots = None
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        explanation.append(f"Calculate the square root of the discriminant: sqrt(D) = {sqrt_discriminant}")
        
        # Calculate the two roots
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        explanation.append(f"Calculate the roots using the quadratic formula:")
        explanation.append(f"x1 = (-{b} + sqrt(D)) / (2*{a}) = {root1}")
        explanation.append(f"x2 = (-{b} - sqrt(D)) / (2*{a}) = {root2}")
        
        roots = (root1, root2)
        explanation.append(f"Solutions: x1 = {root1}, x2 = {root2}")
    
    return roots, "\n".join(explanation)

# Example usage
# roots, explanation = solve_quadratic_equation(1, -3, 2)
# print(explanati