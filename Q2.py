def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Get user input for the matrix
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

# Find the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

# Display the result
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
