def factorial(num):
  result = 1
  for i in range(1,num+1):
    result *= i
  return result
  
def binomial_cofficient(n,k):
  return factorial(n) // (factorial(k) * factorial(n-k))

def count_solution(n,val):
  return binomial_cofficient(n+val-1,n-1)


n = int(input())
val = int(input())
print(count_solution(n,val))