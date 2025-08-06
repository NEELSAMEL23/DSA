def dfs(visited, skip, current, remaining):
    if remaining < 0:
        return 0
    if remaining == 0:
        return 1
    visited[current] = True
    result = 0
    for next_dot in range(1, 10):
        if not visited[next_dot] and (skip[current][next_dot] == 0 or visited[skip[current][next_dot]]):
            result += dfs(visited, skip, next_dot, remaining - 1)
    visited[current] = False
    return result

def unlock_patterns(m, n):
    skip = [[0] * 10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = 5
    skip[2][8] = skip[8][2] = 5
    skip[3][7] = skip[7][3] = 5
    skip[4][6] = skip[6][4] = 5
    skip[1][5] = skip[2][5] = skip[3][5] = skip[4][5] = skip[6][5] = skip[7][5] = skip[8][5] = skip[9][5] = 0

    visited = [False] * 10
    result = 0
    for length in range(m, n + 1):
        result += dfs(visited, skip, 1, length - 1) * 4  # corner
        result += dfs(visited, skip, 2, length - 1) * 4  # edge
        result += dfs(visited, skip, 5, length - 1)      # center
    return result

# Input
m, n = map(int, input().split())
print(unlock_patterns(m, n))
