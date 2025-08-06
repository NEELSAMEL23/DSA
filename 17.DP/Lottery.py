def Lottery(arr,N):
  dp = [[0] * N for _ in range(N)]

  for i in range(N):
    dp[i][i] = arr[i]
    
  for length in range(2,N+1):
    for i in range(N - length + 1):
      j = i + length - 1
      dp[i][j] = max(arr[i] - dp[i+1][j],arr[j] - dp[i][j-1])
      
  return dp[0][N-1]

N = int(input())
arr = list(map(int,input().split()))
res = Lottery(arr,N)
print(res)