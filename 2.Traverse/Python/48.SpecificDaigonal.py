# Function to find and print both diagonals
def find_diagonals(matrix, N, M, K):
    
    # Find the position of the element K
    row = -1
    col = -1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == K:
                row, col = i, j
                break
        if row != -1:
            break
    
    # Collect the left-to-right diagonal (top-left to bottom-right)
    left_to_right_diag = []
    i, j = row, col
    
    # Traverse upwards left
    while i >= 0 and j >= 0:
        left_to_right_diag.insert(0, matrix[i][j])
        i -= 1
        j -= 1
    # Traverse downwards right

    i, j = row + 1, col + 1
    while i < N and j < M:
        left_to_right_diag.append(matrix[i][j])
        i += 1
        j += 1

    # Collect the right-to-left diagonal (top-right to bottom-left)
    right_to_left_diag = []
    i, j = row, col
    # Traverse upwards right
    while i >= 0 and j < M:
        right_to_left_diag.insert(0, matrix[i][j])
        i -= 1
        j += 1
    # Traverse downwards left
    i, j = row + 1, col - 1
    while i < N and j >= 0:
        right_to_left_diag.append(matrix[i][j])
        i += 1
        j -= 1

    # Print the diagonals
    print(" ".join(map(str, left_to_right_diag)))
    print(" ".join(map(str, right_to_left_diag)))

# Example usage:
N = 4
M = 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
K = 11
find_diagonals(matrix, N, M, K)
