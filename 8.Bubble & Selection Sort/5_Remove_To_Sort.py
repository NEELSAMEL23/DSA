arr = [1, 2, 4, 3, 5, 7, 8, 6, 9, 10]

result = []

for num in arr:
    if len(result) == 0 or num >= result[-1]:
        result.append(num)

print(*result)

