def max_cars_same_speed(speeds):
    freq = {}
    
    for speed in speeds:
        if speed in freq:
            freq[speed] += 1
        else:
            freq[speed] = 1

    max_count = 0
    for count in freq.values():
        if count > max_count:
            max_count = count

    return max_count

# Sample Input
n = int(input())
speeds = list(map(int, input().split()))
print(max_cars_same_speed(speeds))
