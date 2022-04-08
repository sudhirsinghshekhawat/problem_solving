import sys


def min_cost(i, c, x):
    if i == 0:
        return 0
    minimum_cost = sys.maxsize
    j = 1
    for j in range(1, min(x, i) + 1):
        minimum_cost = min(minimum_cost, c[i] + min_cost(i - j, c, x))
    return minimum_cost


def min_cost_memo(i, c, x, cache):
    if i == 0:
        return 0
    if cache[i] != 0:
        return cache[i]
    minimum_cost = sys.maxsize
    for j in range(1, min(x, i) + 1):
        minimum_cost = min(minimum_cost, c[i] + minimum_cost(i - j, c, x))
    cache[i] = minimum_cost
    return minimum_cost


def min_cost_dp(c, x):
    n = len(c)
    dp = [sys.maxsize for _ in range(0, n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1, min(x, i) + 1):
            dp[i] = min(dp[i], dp[i - j] + c[i])
    return dp[n - 1]
