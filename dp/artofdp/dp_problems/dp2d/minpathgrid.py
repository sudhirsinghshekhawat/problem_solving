import sys


def min_path(i, j, grid):
    if i == 0 and j == 0:
        return grid[0][0]
    min_cost = sys.maxsize
    if i > 0:
        min_cost = min_path(i - 1, j, grid) + grid[i][j]
    if j > 0:
        min_cost = min(min_cost, min_path(i, j - 1, grid) + grid[i][j])

    return min_cost


def min_path_memo(i, j, grid, cache):
    if i == 0 and j == 0:
        return grid[0][0]
    if cache[i][j] != -1:
        return cache[i][j]
    min_cost = sys.maxsize
    if i > 0:
        min_cost = min_path(i - 1, j, grid) + grid[i][j]
    if j > 0:
        min_cost = min(min_cost, min_path(i, j - 1, grid) + grid[i][j])
    cache[i][j] = min_cost
    return cache[i][j]


def min_path_dp(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = sys.maxsize
            if i > 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
    return dp[m - 1][n - 1]
