def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(mat, x, y, dest_x, dest_y, visited):
    if x == dest_x and y == dest_y:
        return 0  # Reached destination, don't count this cell either

    max_candies = -1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    visited[x][y] = True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, len(mat), len(mat[0])) and not visited[nx][ny] and mat[nx][ny] != 0:
            candies = mat[nx][ny] + dfs(mat, nx, ny, dest_x, dest_y, visited)
            if candies >= 0:
                max_candies = max(max_candies, candies)

    visited[x][y] = False  # Backtrack
    return max_candies

# Input reading
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

bob_x, bob_y = map(int, input().split())
shop_x, shop_y = map(int, input().split())

visited = [[False]*m for _ in range(n)]

# Mark start as visited and start DFS from Bob's position
result = dfs(mat, bob_x, bob_y, shop_x, shop_y, visited)

if result == -1:
    print(-1)
else:
    print(result)
