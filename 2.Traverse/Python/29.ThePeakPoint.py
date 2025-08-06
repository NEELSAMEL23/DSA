def findpeakpoint(arr,n):
  
  for i in range(1,len(arr)-1):
    if(arr[i]>arr[i-1] and arr[i] > arr[i+1]):
      return i
  return - 1
    
t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  res = findpeakpoint(arr,n)
  print(res)    