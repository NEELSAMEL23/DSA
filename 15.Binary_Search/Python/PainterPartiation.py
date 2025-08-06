def is_possible(arr, n, p, max_len):
    painter_count = 1
    current_sum = 0

    for length in arr:
        if length > max_len:
            return False  # cannot assign this board to any painter
        if current_sum + length <= max_len:
            current_sum += length
        else:
            painter_count += 1
            current_sum = length
            if painter_count > p:
                return False
    return True


def min_time(arr, n, p):
    low = max(arr)
    high = sum(arr)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, n, p, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_time(arr, n, p))
