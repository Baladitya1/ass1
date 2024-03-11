def matrix_multiply(A, B):
    # Get the number of rows and columns of matrices A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Check if the number of columns in A equals the number of rows in B for matrix multiplication
    if cols_A == rows_B:
        # Initialize the resulting matrix C with zeros
        C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
        
        # Perform matrix multiplication
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    # Update each element of C
                    C[i][j] += A[i][k] * B[k][j]
        
        # Print the resulting matrix C
        print(C)
    else:
        print("Cannot multiply matrices. Number of columns in matrix A must be equal to the number of rows in matrix B.")

# Define matrices X and Y
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

matrix_multiply(X, Y)
