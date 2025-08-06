N = 3
X = 2

sum = 0
for i in range(N):
    sum += X ** i

print(sum)

# DRY RUN:
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# sum = 1 + 2 + 4 = 7
