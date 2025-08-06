s = input().strip()
n = len(s)
i = 0
result = 0

while i < n:
    count = 1
 
    while i + 1 < n and s[i] == s[i + 1]:
        count += 1
        i += 1

    result += (count * (count + 1)) // 2
    i += 1

print(result)
