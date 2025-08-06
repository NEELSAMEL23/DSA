def remaining_chocolates(a,b):
  
  while b !=0:
    a,b = b , a % b
  return a

t = int(input())

for _ in range(t):
  x , y = map(int,input().split())
  print(2 * remaining_chocolates(x,y))