import sys


def max_profit(l, p):
    if l == 0:
        return 0
    max_p = -sys.maxsize
    for i in range(l):
        max_p = max(max_p, p[i] + max_profit(l - i - 1, p))
    return max_p


def max_profit_mem(l, p, cache):
    if l == 0:
        return 0
    if cache[l] != -1:
        return cache[l]
    max_p = -sys.maxsize
    for i in range(l):
        max_p = max(max_p, p[i] + max_profit_mem(l - i - 1, p, cache))
        cache[l] = max_p
    return cache[l]


def max_profit_dp(l, p):
    dp = [0 for _ in range(l + 1)]
    max_p = -sys.maxsize
    for i in range(1, l+1):
        dp[i] = -sys.maxsize
        for j in range(i):
            dp[i] = max(max_p, p[i] + dp[i - j - 1])
    return dp[l]
