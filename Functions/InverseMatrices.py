def inverse_matrix(A):
    """
    Calculates the inverse of a matrix.

    Parameters:
    - A: matrix

    Returns:
    - result: inverse of A
    - explanation: step-by-step explanation
    """
    import numpy as np
    result = np.linalg.inv(A)
    explanation = f"Inverse Matrix: inv(A) = {result}"
    return result, explanation

# Example usage
#A = [[1, 2], [3, 4]]
#result, explanation = inverse_matrix(A)
#print(explanation)
