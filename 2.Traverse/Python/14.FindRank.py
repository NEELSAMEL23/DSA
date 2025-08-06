def Find_Rank(arr,N):

  for i in range(N):
    if arr[i] == "India":
      return i + 1





arr = ["Russia",'USA',"Japan","China","India"]
N = 5
res = Find_Rank(arr,N)
print(res)