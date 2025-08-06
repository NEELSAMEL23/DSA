import math
def EatOranges(N,K,piles):
  left = 1
  right = max(piles)
  result = right
  
  while left <= right:
    mid = (left + right) // 2
    
    hours_needed = sum(math.ceil(pile/mid) for pile in piles)
    
    if hours_needed <= K :
      result = mid
      right = mid - 1
    else:
      left = mid + 1
  
  return result




t = int(input())
for i in range(t):
  N,K = map(int,input().split())
  piles = list(map(int,input().split()))
  res = EatOranges(N,K,piles)
  print(res)