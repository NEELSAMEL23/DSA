def count_sum_occurrences(matrix, n, m, s):
    count = 0
    
    # Horizontal check
    for i in range(n):
        for j in range(m - 2):
            if matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] == s:
                count += 1

    # Vertical check
    for i in range(n - 2):
        for j in range(m):
            if matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] == s:
                count += 1

    # Diagonal checks
    # Major diagonal
    for i in range(n - 2):
        for j in range(m - 2):
            if matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] == s:
                count += 1

    # Minor diagonal
    for i in range(2, n):
        for j in range(m - 2):
            if matrix[i][j] + matrix[i - 1][j + 1] + matrix[i - 2][j + 2] == s:
                count += 1

    return count

# Input example
n = 3
m = 3
s = 6
matrix = [
    [3, 2, 1],
    [2, 2, 2],
    [1, 5, 1]
]

# Calculate the result
result = count_sum_occurrences(matrix, n, m, s)         
print(result)  # Expected output: 4
