def solve_linear_equation(a, b, c):
    """
    Solves the linear equation ax + b = c for x.

    Parameters:
    - a: coefficient of x
    - b: constant term
    - c: right-hand side constant

    Returns:
    - x: solution for x
    - explanation: step-by-step explanation of the solution process
    """
    explanation = []
    explanation.append(f"Starting with the equation: {a}x + {b} = {c}")
    
    # Isolate the x term
    explanation.append(f"Subtract {b} from both sides: {a}x = {c} - {b}")
    right_side = c - b
    explanation.append(f"Simplify: {a}x = {right_side}")
    
    # Solve for x
    x = right_side / a
    explanation.append(f"Divide both sides by {a}: x = {right_side}/{a}")
    explanation.append(f"Solution: x = {x}")
    
    return x, "\n".join(explanation)

# Example usage
# x, explanation = solve_linear_equation(2, 3, 7)
# print(explanati