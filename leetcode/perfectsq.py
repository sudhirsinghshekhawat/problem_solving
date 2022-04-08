from math import sqrt


def solve(n):
    if n <= 3:
        return n
    ans = n
    for i in range(1, int(sqrt(n)) + 1):
        ans = min(ans, 1 + solve(n - (i * i)))
    return ans


def solve_dp(n):
    if n <= 3:
        return n
    dp = [i for i in range(n + 1)]
    for i in range(n+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], 1 + dp[i - (j * j)])
            j += 1
    return dp[n]


result = solve(13)
print(result)
result = solve_dp(13)
print(result)
