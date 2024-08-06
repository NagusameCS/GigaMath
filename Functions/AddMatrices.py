def matrix_add(A, B):
    """
    Adds two matrices.

    Parameters:
    - A: first matrix
    - B: second matrix

    Returns:
    - result: sum of A and B
    - explanation: step-by-step explanation
    """
    result = []
    explanation = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
            explanation.append(f"({A[i][j]} + {B[i][j]}) ")
        result.append(row)
        explanation.append("\n")
    
    explanation.append(f"= {result}")
    return result, ''.join(explanation)

# Example usage
#A = [[1, 2], [3, 4]]
#B = [[5, 6], [7, 8]]
#result, explanation = matrix_add(A, B)
#print(explanation)
