def determinant(A):
    """
    Calculates the determinant of a matrix.

    Parameters:
    - A: matrix

    Returns:
    - result: determinant of A
    - explanation: step-by-step explanation
    """
    import numpy as np
    result = np.linalg.det(A)
    explanation = f"Determinant: det(A) = {result}"
    return result, explanation

# Example usage
#A = [[1, 2], [3, 4]]
#result, explanation = determinant(A)
#print(explanation)
