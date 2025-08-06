def sum_without_borders(matrix,N,M):

  total_sum = 0

  for i in range(1,N-1):
    for j in range(1,M-1):
      total_sum += matrix[i][j]
  return total_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
N = 3
M = 3
res = sum_without_borders(matrix,N,M)
print(res)