def Binary_Equivalent(N):
    if N == 0:
        return 0

    result = ""
    while N > 0:
        result = str(N%2) + result
        N = N//2
    return result


N = 15
res = Binary_Equivalent(N)
print(res)