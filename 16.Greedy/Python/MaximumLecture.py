n = int(input())
lectures = []

for _ in range(n):
    start, end = map(int, input().split())
    lectures.append((start, end))

# Sort by end time
lectures.sort(key=lambda x: x[1])

count = 0
last_end_time = 0

for start, end in lectures:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
