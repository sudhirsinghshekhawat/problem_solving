def min_delete(i, j, s):
    if i >= j:
        return 0
    if s[i] == s[j]:
        return min_delete(i + 1, j - 1, s)
    else:
        return 1 + min(min_delete(i + 1, j, s), min_delete(i, j - 1, s))


def min_delete_memo(i, j, s, cache):
    if i >= j:
        return 0
    if cache[i][j] != -1:
        return cache[i][j]
    if s[i] == s[j]:
        cache[i][j] = min_delete(i + 1, j - 1, s, cache)
        return cache[i][j]
    else:
        cache[i][j] = min(min_delete(i + 1, j, s, cache), min_delete(i, j - 1, s, cache)) + 1
        return cache[i][j]


def min_delete_dp(s):
    N = len(s)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1
    for l in range(2, N + 1):
        for i in range(N - l + 1):
            j = i+l - 1
            if s[i] == s[j] and l == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][N - 1]


if __name__ == '__main__':
    string = "suds"
    result = min_delete(0, len(string) - 1, string)
    print(result)
    result = min_delete_dp(string)
    print(result)
    # result = min_delete_dp(string)
    # print(result)
