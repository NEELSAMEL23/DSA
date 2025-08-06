def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])  # Path compression
    return parent[a]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA == rootB:
        return False  # Edge forms a cycle
    parent[rootB] = rootA
    return True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    cycle_count = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if not union(parent, a, b):
            cycle_count += 1
    print(cycle_count)
