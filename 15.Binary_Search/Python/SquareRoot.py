def floor_sqrt(n):
    if n < 2:
        return n
    low = 1
    high = n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(floor_sqrt(N))


for res in results:
    print(res)
