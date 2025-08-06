def minPenalty(arr,k):
  def is_possible(mid):
    moves = 0
    for blocks in arr:
      
      moves += (blocks - 1) // mid
      
      if moves > k:
        return False
    return moves <=k
    
    
  
  left , right = 1 , max(arr)
  
  while left < right:
    mid = (left + right) // 2
    if is_possible(mid):
      right = mid
    else:
      left = mid + 1
  
  return left





t = int(input())

for _ in range(t):
  
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  
  print(minPenalty(arr,k))