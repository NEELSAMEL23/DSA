def can_cut(planks, k, length):
    count = 0
    for plank in planks:
        count += plank // length
    return count >= k

def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # Number of planks and required pieces
        planks = list(map(int, input().split()))  # Plank lengths

        low, high = 1, max(planks)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_cut(planks, k, mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        print(result)

# Run the solve function
solve()
