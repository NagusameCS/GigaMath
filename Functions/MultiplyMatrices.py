def multiply_matrices(A, B):
    """
    Multiplies two matrices A and B.

    Parameters:
    - A: matrix represented as a list of lists (2D list)
    - B: matrix represented as a list of lists (2D list)

    Returns:
    - C: resulting matrix from multiplying A and B
    - explanation: step-by-step explanation of the multiplication process
    """
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_cols_B = len(B[0])
    
    # Initialize the result matrix C with zeros
    C = [[0 for _ in range(num_cols_B)] for _ in range(num_rows_A)]
    explanation = []
    
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            explanation.append(f"Calculating C[{i}][{j}]:")
            for k in range(num_cols_A):
                explanation.append(f"  Adding A[{i}][{k}] * B[{k}][{j}] = {A[i][k]} * {B[k][j]}")
                C[i][j] += A[i][k] * B[k][j]
            explanation.append(f"  Result C[{i}][{j}] = {C[i][j]}")
    
    return C, "\n".join(explanation)

# Example usage
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[7, 8], [9, 10], [11, 12]]
# C, explanation = multiply_matrices(A, B)
# print(expla