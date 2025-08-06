import sys

def uniquePathsWithObstacles(m: int, n: int, grid: list[list[int]]) -> int:
    """
    Calculates the number of unique paths from the top-left corner to the
    bottom-right corner of a grid with obstacles.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.
        grid: A list of lists representing the grid, where 0 is a free space
              and 1 is an obstacle.

    Returns:
        The number of unique paths modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    # Create a DP table initialized with zeros.
    # dp[i][j] will store the number of unique paths to reach cell (i, j).
    dp = [[0] * n for _ in range(m)]

    # Handle the starting cell.
    # If the starting cell itself is an obstacle, there are no paths.
    if grid[0][0] == 1:
        return 0
    else:
        dp[0][0] = 1 # One way to be at the starting point if it's not an obstacle

    # Fill the first row (robot can only move right)
    for j in range(1, n):
        # If the current cell is not an obstacle AND the previous cell was reachable
        if grid[0][j] == 0 and dp[0][j-1] == 1: # dp[0][j-1] == 1 means previous cell is reachable
            dp[0][j] = 1
        # If grid[0][j] is an obstacle, dp[0][j] remains 0 (default initialized value)
        # If dp[0][j-1] is 0, it means all cells to the right are also unreachable

    # Fill the first column (robot can only move down)
    for i in range(1, m):
        # If the current cell is not an obstacle AND the previous cell was reachable
        if grid[i][0] == 0 and dp[i-1][0] == 1: # dp[i-1][0] == 1 means previous cell is reachable
            dp[i][0] = 1
        # If grid[i][0] is an obstacle, dp[i][0] remains 0
        # If dp[i-1][0] is 0, it means all cells below are also unreachable

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            # If the current cell is an obstacle, it's unreachable (0 paths)
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                # Number of paths to (i, j) is the sum of paths from (i-1, j) (down)
                # and paths from (i, j-1) (right).
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

    # The result is the number of paths to the bottom-right corner
    return dp[m-1][n-1]

# Example Usage (for local testing purposes)
if __name__ == '__main__':
    # Sample Input 1:
    # 3 3
    # 0 0 0
    # 0 1 0
    # 0 0 0
    m1 = 3
    n1 = 3
    grid1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    result1 = uniquePathsWithObstacles(m1, n1, grid1)
    print(f"Sample 1 Output: {result1}") # Expected Output: 2

    # Example: Grid with no obstacles
    m2 = 2
    n2 = 2
    grid2 = [
        [0, 0],
        [0, 0]
    ]
    result2 = uniquePathsWithObstacles(m2, n2, grid2)
    print(f"Sample 2 Output (no obstacles): {result2}") # Expected Output: 2 (R-D, D-R)

    # Example: Grid with obstacle at start
    m3 = 3
    n3 = 3
    grid3 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result3 = uniquePathsWithObstacles(m3, n3, grid3)
    print(f"Sample 3 Output (obstacle at start): {result3}") # Expected Output: 0

    # Example: Grid with obstacle at end
    m4 = 3
    n4 = 3
    grid4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    result4 = uniquePathsWithObstacles(m4, n4, grid4)
    print(f"Sample 4 Output (obstacle at end): {result4}") # Expected Output: 0
