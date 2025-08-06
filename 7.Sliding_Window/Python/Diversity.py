t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    incomes.sort()

    i = 0
    max_families = 0

    for j in range(n):
        while incomes[j] - incomes[i] > k:
            i += 1
        max_families = max(max_families, j - i + 1)

    print(max_families)
