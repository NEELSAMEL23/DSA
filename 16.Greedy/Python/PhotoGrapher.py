
def arrange_people(n,x,heights):
  
  heights.sort()
  
  front_row = heights[:n]
  back_row = heights[n:]
  
  for i in range(n):
    if back_row[i] - front_row[i] < x:
      return "NO"
    else:
      return "YES"


t = int(input())

for _ in range(t):
  
  n , x = map(int,input().split())
  
  heights = list(map(int,input().split()))
  
  res = arrange_people(n,x,heights)
  print(res)