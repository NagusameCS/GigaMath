def derivative_of_polynomial(coefficients):
    """
    Calculates the derivative of a polynomial function.

    Parameters:
    - coefficients: list of coefficients [a_n, a_{n-1}, ..., a_0]

    Returns:
    - derivative_coefficients: list of coefficients of the derivative
    - explanation: step-by-step explanation of the differentiation process
    """
    explanation = []
    explanation.append("Given polynomial coefficients: " + str(coefficients))
    
    derivative_coefficients = []
    degree = len(coefficients) - 1
    
    for i in range(len(coefficients) - 1):
        coefficient = coefficients[i]
        power = degree - i
        derivative_coefficients.append(coefficient * power)
        explanation.append(f"Take the derivative of {coefficient}x^{power}: {coefficient} * {power} = {coefficient * power}")
    
    explanation.append("The derivative of the polynomial is given by the coefficients: " + str(derivative_coefficients))
    
    return derivative_coefficients, "\n".join(explanation)

# Example usage
# coefficients = [3, -4, 2]  # 3x^2 - 4x + 2
# derivative, explanation = derivative_of_polynomial(coefficients)
# print(explana