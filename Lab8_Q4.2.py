def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Input for the first matrix
rows1 = int(input("Enter the number of rows for Matrix 1: "))
cols1 = int(input("Enter the number of columns for Matrix 1: "))
matrix1 = input_matrix(rows1, cols1)

# Input for the second matrix
rows2 = int(input("Enter the number of rows for Matrix 2: "))
cols2 = int(input("Enter the number of columns for Matrix 2: "))
matrix2 = input_matrix(rows2, cols2)

# Display matrices
print("\nMatrix 1:")
display_matrix(matrix1)
print("\nMatrix 2:")
display_matrix(matrix2)

# Multiplication of matrices
if cols1 == rows2:
    product_matrix = multiply_matrices(matrix1, matrix2)
    print("\nProduct Matrix:")
    display_matrix(product_matrix)
else:
    print("\nMatrices cannot be multiplied. Number of columns in Matrix 1 is not equal to the number of rows in Matrix 2.")
