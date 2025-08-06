A = [12,18,17,65,46]
k = 6

A.sort(key=lambda x: x % k)

print(" ".join(map(str, A)))