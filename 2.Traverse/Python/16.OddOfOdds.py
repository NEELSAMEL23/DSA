def Odd_Count(arr,N):
  Odd_count = 0
  
  for i in range(N):
    if arr[i] % 2 !=0:
      Odd_count+=1

  if Odd_count % 2!=0:
    return "YES"
  return "NO"

arr = [1,101]
N = 2

res = Odd_Count(arr,N)
print(res)