# Input for matrix dimension
n = int(input("Enter the dimension of the square matrix (N): "))

# Input for the matrix
matrix = []
print(f"Enter elements for a {n}x{n} matrix:")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert the matrix to row echelon form
current_column = 0

for row in range(n):
    # Find the first non-zero element in the current row
    while current_column < n and matrix[row][current_column] == 0:
        current_column += 1

    # If all elements in the current column are zero, move to the next column
    if current_column == n:
        continue

    # If the non-zero element is not in the current row, swap rows
    if matrix[row][current_column] != 1:
        for i in range(row + 1, n):
            if matrix[i][current_column] == 1:
                matrix[row], matrix[i] = matrix[i], matrix[row]
                break

    # Normalize the current row
    pivot = matrix[row][current_column]
    matrix[row] = [element / pivot for element in matrix[row]]

    # Eliminate non-zero elements below the pivot
    for i in range(row + 1, n):
        factor = matrix[i][current_column]
        matrix[i] = [a - factor * b for a, b in zip(matrix[i], matrix[row])]

    # Increment current_column
    current_column += 1

# Display the matrix in row echelon form
print("\nMatrix in Row Echelon Form:")
for row in matrix:
    print(row)
