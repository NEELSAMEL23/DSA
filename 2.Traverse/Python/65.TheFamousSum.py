def superDigit(n,k):
  
  total = sum(int(d) for d in n) * k
  
  while total >= 10:
    total = sum(int(d) for d in str(total))

  return total



n , k = input().split()
k = int(k)
res = superDigit(n,k)
print(res)