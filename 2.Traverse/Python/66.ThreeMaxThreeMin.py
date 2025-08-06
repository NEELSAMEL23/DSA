n = int(input())
arr = list(map(int, input().split()))

unique_values = sorted(set(arr))

# Check if at least 3 distinct values exist
if len(unique_values) < 3:
    print("Not Possible")
else:
    print(*unique_values[:3])

if len(unique_values) < 3:
    print("Not Possible")
else:
    print(*unique_values[-3:])
