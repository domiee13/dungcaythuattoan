# Check if the given matrix is diagonal.

# Example

# For

# matrix = [[1, 0, 0], 
#           [0, 5, 0], 
#           [0, 0, 3]]
# the output should be
# isDiagonalMatrix(matrix) = true;

# For

# matrix = [[1, 0, 0], 
#           [0, 5, 0], 
#           [2, 0, 3]]
# the output should be
# isDiagonalMatrix(matrix) = false.
def isDiagonalMatrix(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and i!=j:
                return False
    return True
