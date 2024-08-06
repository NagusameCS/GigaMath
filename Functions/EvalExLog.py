import math

def evaluate_exponential_logarithmic(x):
    """
    Evaluates the exponential function e^x and the natural logarithm ln(x).
    
    Parameters:
    - x: input value
    
    Returns:
    - exp_x: value of e^x
    - ln_x: value of ln(x) or None if x <= 0
    - explanation: step-by-step explanation of the calculations
    """
    explanation = []
    explanation.append(f"Given input value: x = {x}")
    
    # Exponential function e^x
    exp_x = math.exp(x)
    explanation.append(f"Exponential: e^{x} = {exp_x}")
    
    # Natural logarithm ln(x)
    if x > 0:
        ln_x = math.log(x)
        explanation.append(f"Natural logarithm: l