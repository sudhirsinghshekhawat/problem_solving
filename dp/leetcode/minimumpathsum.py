import sys


def min_path_sum(arr):
    return min_path_sum_recursion(arr, 0, 0)


def min_path_sum_recursion(arr, i, j):
    m = len(arr) - 1
    n = len(arr[0]) - 1
    result = arr[i][j]

    if i == m and j == n:
        return result
    if i == m and j != n:
        return result + min_path_sum_recursion(arr, i, j + 1)

    if i != m and j == n:
        return result + min_path_sum_recursion(arr, i + 1, j)

    return result + min(min_path_sum_recursion(arr, i, j + 1),
                        min_path_sum_recursion(arr, i + 1, j))


def min_path_sum_top_down(grid, memo, i, j):
    m = len(grid) - 1
    n = len(grid[0]) - 1
    n = len(grid[0]) - 1

    if i == m and j == n:
        return grid[i][j]
    if i == m or j == n:
        return sys.maxsize

    result = grid[i][j] + min(min_path_sum_top_down(grid, memo, i + 1, j),
                              min_path_sum_top_down(grid, memo, i, j + 1))
    memo[i][j] = result
    return memo[i][j]


def min_path_sum_memo(grid):
    memo = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return min_path_sum_top_down(grid, memo, 0, 0)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
result = min_path_sum(grid)
print(result)

result = min_path_sum_memo(grid)
print(result)
