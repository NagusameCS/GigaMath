import numpy as np

class LinearAlgebra:
    @staticmethod
    def matrix_add(matrix1, matrix2):
        result = np.add(matrix1, matrix2)
        explanation = f"The sum of matrices is {result}."
        return result, explanation

    @staticmethod
    def matrix_multiply(matrix1, matrix2):
        result = np.dot(matrix1, matrix2)
        explanation = f"The product of matrices is {result}."
        return result, explanation

    @staticmethod
    def determinant(matrix):
        result = np.linalg.det(matrix)
        explanation = f"The determinant of the matrix is {result}."
        return result, explanation

    @staticmethod
    def inverse_matrix(matrix):
        try:
            result = np.linalg.inv(matrix)
            explanation = f"The inverse of the matrix is {result}."
        except np.linalg.LinAlgError:
            return None, "Matrix is singular and cannot be inverted."
        return result, explanation
