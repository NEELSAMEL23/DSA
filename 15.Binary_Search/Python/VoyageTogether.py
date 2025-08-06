def canShipwithDays(nums,k,capacity):
  
  days = 1
  current_load = 0
  
  for num in nums:
    if current_load + num > capacity:
      days += 1
      current_load = num
      if days > k:
        return False
    else:
      current_load += num
      
  return True
    

def minShipsCapacity(nums,N,K):
  
  left , right = max(nums),sum(nums)
  
  while left < right:
    mid = (left + right) // 2
    if canShipwithDays(nums,K,mid):
      right = mid
    else:
      left = mid + 1
  
  return left
  
  

t = int(input())

for i in range(t):
  N , K = map(int,input().split())
  arr = list(map(int,input().split()))
  
  res = minShipsCapacity(arr,N,K)
  print(res)