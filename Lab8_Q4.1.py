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

def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
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

# Addition of matrices
sum_matrix = add_matrices(matrix1, matrix2)
print("\nSummation Matrix:")
display_matrix(sum_matrix)


