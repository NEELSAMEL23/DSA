def factorial(N):
    if N == 1:
        return 1
    else:
        return N*factorial(N-1)

N = 5
res = factorial(N)
print(res)

