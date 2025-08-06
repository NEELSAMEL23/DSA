def SquareRootSorting(arr,N):
  
  return sorted(arr,key=lambda x: (int(abs(x) ** 0.5), x))
  
t = int(input())

for _ in range(t):
  N = int(input())
  arr = list(map(int,input().split()))
  
  res = SquareRootSorting(arr,N)
  print(*res)