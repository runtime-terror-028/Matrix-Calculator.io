def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det

def scalar_multiply(matrix, scalar):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return [[scalar * matrix[i][j] for j in range(cols)] for i in range(rows)]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

def subtract_matrices(mat1, mat2):
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

def multiply_matrices(mat1, mat2):
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
