def changeArray(arr,n):
  low = min(arr)
  
  res = [-1 if x % low ==0 else x for x in arr]
  
  return res
  
t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  res = changeArray(arr,n)
  print(*res)