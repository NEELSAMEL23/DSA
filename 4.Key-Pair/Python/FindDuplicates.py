def solve(N, k, A):
    last_seen = {}

    for i in range(N):
        if A[i] in last_seen and i - last_seen[A[i]] <= k:
            print(last_seen[A[i]] + 1, i + 1)
            return
        last_seen[A[i]] = i

    print(-1)
