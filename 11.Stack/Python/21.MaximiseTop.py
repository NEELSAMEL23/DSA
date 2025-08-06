def maximize_top(N, K, stack):
    if N == 0:
        return -1

    if K == 0:
        return stack[0]
    
    if K == 1:
        if N >= 2:
            return stack[1]
        else:
            return -1

    if K > N:
        return max(stack)

    if K == N:
        return max(stack[:K-1])

    return max(max(stack[:K-1]), stack[K]) if K < N else max(stack[:K-1])


# Hardcoded input
N = 6
K = 4
stack = [1,2,4,3,3,5]

result = maximize_top(N, K, stack)
print(result)
