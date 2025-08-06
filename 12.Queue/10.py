n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
t = 0
k -= 1  
for i in range(len(arr)):
    if i <= k:
        t += min(arr[i], arr[k])
    else:
        t += min(arr[i], arr[k] - 1)
print(t)