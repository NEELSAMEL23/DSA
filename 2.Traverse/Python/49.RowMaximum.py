def max_Row(arr,N,M):
  mat = []
  
  for i in range(N):
    max_row = 0
    for j in range(M):
      if  arr[i][j] > max_row:
        max_row = arr[i][j]
    mat.append(max_row)
        
  return mat
    
N = 3
M = 3
arr = [
  [1,2,3],[4,5,6],[7,8,9]
]

res = max_Row(arr,N,M)
print(*res)