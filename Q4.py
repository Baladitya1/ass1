def transpose(A):
    # Iterate through the rows of matrix A
    for i in range(len(A)):
        # Iterate through the columns of matrix A
        for j in range(len(A)):
            # Check if the current element's row index is greater than its column index
            if i > j:
                # Swap the elements at positions (i, j) and (j, i)
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
    
    # Print the transposed matrix
    print(A)

# Define matrix 
X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

# Call the transpose function
transpose(X)
