def binomial_cofficient_rec(n, k):
    if n == k or k == 0:
        return 1
    return binomial_cofficient_rec(n - 1, k - 1) + binomial_cofficient_rec(n - 1, k)


def binomial_cofficient_mem(n, k, mem):
    if n == k or k == 0:
        return 1
    if mem[n][k] != 0:
        result = binomial_cofficient_mem(n - 1, k - 1, mem) + binomial_cofficient_mem(n - 1, k, mem)
        mem[n][k] = result
    return mem[n][k]


def binomial_coficient_dp(n, k):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = 1
        if i <= k:
            dp[i][i] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]
