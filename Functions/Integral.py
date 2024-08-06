def integral(f, a, b, n=1000):
    """
    Calculates the numerical integral of a function over an interval [a, b].

    Parameters:
    - f: the function
    - a: lower bound
    - b: upper bound
    - n: number of subintervals (default: 1000)

    Returns:
    - result: integral of f from a to b
    - explanation: step-by-step explanation
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    explanation = [f"Integral: Sum = 0.5*(f({a}) + f({b}))"]
    
    for i in range(1, n):
        result += f(a + i * h)
        explanation.append(f" + f({a} + {i}*{h})")
    
    result *= h
    explanation.append(f") * {h} = {result}")
    return result, ''.join(explanation)

# Example usage
# f = lambda x: x**2
# result, explanation = integral(f, 0, 1)
# print(explanation)
