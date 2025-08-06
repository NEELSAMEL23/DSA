def smallestFrequency(matrix,N):
  diagElemen = []
  
  for i in range(N):
    diagElemen.append(matrix[i][i])
    diagElemen.append(matrix[i][N-1-i]) 
            
  min_val = min(diagElemen)
  res = diagElemen.count(min_val)
  return res

t = int(input())

for _ in range(t):
  N = int(input())
  matrix = [list(map(int,input().split())) for _ in range(N)]
  res = smallestFrequency(matrix,N)
  print(res)