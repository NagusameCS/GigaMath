def integrate_polynomial(coefficients):
    """
    Calculates the indefinite integral of a polynomial function.

    Parameters:
    - coefficients: list of coefficients [a_n, a_{n-1}, ..., a_0]

    Returns:
    - integral_coefficients: list of coefficients of the integral
    - explanation: step-by-step explanation of the integration process
    """
    explanation = []
    explanation.append("Given polynomial coefficients: " + str(coefficients))
    
    integral_coefficients = []
    degree = len(coefficients) - 1
    
    for i in range(len(coefficients)):
        coefficient = coefficients[i]
        power = degree - i + 1
        integral_coefficients.append(coefficient / power)
        explanation.append(f"Integrate {coefficient}x^{degree - i}: {coefficient}/{power}x^{power}")
    
    integral_coefficients.append("C")  # Constant of integration
    explanation.append("The indefinite integral of the polynomial is given by the coefficients: " + str(integral_coefficients))
    
    return integral_coefficients, "\n".join(explanation)

# Example usage
# coefficients = [3, -4, 2]  # 3x^2 - 4x + 2
# integral, explanation = integrate_polynomial(coefficients)
# print(explana