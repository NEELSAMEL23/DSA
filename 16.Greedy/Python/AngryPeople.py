from collections import deque

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

q = deque()

# Alternate inserting smallest/largest values
for i in range(n):
    if i % 2 == 0:
        q.appendleft(arr[i])
    else:
        q.append(arr[i])

# Now calculate the max difference between adjacent people
danger = 0
for i in range(n):
    diff = abs(q[i] - q[(i+1) % n])
    danger = max(danger, diff)

print(danger)
