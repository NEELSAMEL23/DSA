def move_zeros(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    print(*non_zeros + zeros)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    move_zeros(arr)
