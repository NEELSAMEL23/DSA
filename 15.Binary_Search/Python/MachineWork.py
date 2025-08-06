def min_days_to_produce(machines, goal):
    low = 1
    high = max(machines) * goal

    while low < high:
        mid = (low + high) // 2
        total = sum(mid // machine for machine in machines)
        
        if total >= goal:
            high = mid
        else:
            low = mid + 1

    return low

# Reading input
n, goal = map(int, input().split())
machines = list(map(int, input().split()))

# Output the minimum number of days
print(min_days_to_produce(machines, goal))
