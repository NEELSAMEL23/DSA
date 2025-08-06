

def solve(n, k, arr):
    k = k % n  
    arr = arr[n - k:] + arr[:n - k]
    print(*arr)
t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(n, k, arr)
