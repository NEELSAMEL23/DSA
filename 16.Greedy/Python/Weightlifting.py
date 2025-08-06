t = int(input())
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))

    left = 0
    right = n - 1
    harry_total = 0
    john_total = 0
    turn = 0
    last_weight = 0

    while left <= right:
        if turn % 2 == 0: 
            current = 0
            while left <= right and current <= last_weight:
                current += weights[left]
                left += 1
            harry_total += current
            last_weight = current
        else: 
            current = 0
            while left <= right and current <= last_weight:
                current += weights[right]
                right -= 1
            john_total += current
            last_weight = current
        turn += 1

    print(harry_total, john_total)
