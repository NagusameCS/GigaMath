import math

def evaluate_trigonometric_functions(angle_degrees):
    """
    Evaluates the sine, cosine, and tangent of an angle in degrees.

    Parameters:
    - angle_degrees: angle in degrees

    Returns:
    - sine: sine of the angle
    - cosine: cosine of the angle
    - tangent: tangent of the angle
    - explanation: step-by-step explanation of the calculations
    """
    explanation = []
    explanation.append(f"Given angle: {angle_degrees} degrees")
    
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    explanation.append(f"Convert to radians: {angle_degrees} * π/180 => {angle_radians}")
    
    # Calculate sine
    sine = math.sin(angle_radians)
    explanation.append(f"Sine: sin({angle_degrees}°) => sin({angle_radians}) => {sine}")
    
    # Calculate cosine
    cosine = math.cos(angle_radians)
    explanation.append(f"Cosine: cos({angle_degrees}°) => cos({angle_radians}) => {cosine}")
    
    # Calculate tangent
    tangent = math.tan(angle_radians)
    explanation.append(f"Tangent: tan({angle_degrees}°) => tan({angle_radians}) => {tangent}")
    
    return sine, cosine, tangent, "\n".join(explanation)

# Example usage
# angle = 45
# sine, cosine, tangent, explanation = evaluate_trigonometric_functions(angle)
# print(