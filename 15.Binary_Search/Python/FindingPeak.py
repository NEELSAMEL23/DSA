def find_peak(arr):
    n = len(arr)
    for i in range(n):
        left = arr[i - 1] if i - 1 >= 0 else float('-inf')
        right = arr[i + 1] if i + 1 < n else float('-inf')
        if arr[i] > left and arr[i] > right:
            return i
    return -1

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(find_peak(arr))
