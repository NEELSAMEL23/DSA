def Binary_Matrix(arr,N,M):

  for i in range(N):
    matrix = []
    for j in range(M):
      if  arr[i][j] == 1:
        matrix.append(0) 
      else:
        matrix.append(1)
        
    print(*matrix)
  


arr = [[1,0],[0,1],[1,1]]
N = 3
M = 2
Binary_Matrix(arr,N,M)
