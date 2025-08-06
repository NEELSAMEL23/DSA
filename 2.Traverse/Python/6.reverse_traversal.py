def reverse_traversal(n, arr):
  matrix = []
  for i in range(n-1,-1,-1):
    matrix.append(arr[i])
  
  return matrix

n=5
arr = [1, 3, 2, 4, 5]
res =  reverse_traversal(n, arr)
print(*res)