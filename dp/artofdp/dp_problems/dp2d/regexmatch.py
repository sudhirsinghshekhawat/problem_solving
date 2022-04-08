def matche(i, j, s, r):
    if (i == -1 and j == -1) or r[0:j + 1] == '*':
        return True
    if i == -1 or j == -1:
        return False
    if s[i] == r[j]:
        return matche(i - 1, j - 1, s, r)
    elif r[j] == '.':
        return matche(i - 1, j - 1, s, r)
    elif r[j] == '*':
        return matche(i - 1, j, s, r) or matche(i, j - 1, s, r)
    return False


def matches_memo(i, j, s, r, cache):
    if (i == -1 and j == -1) or r[0:j + 1] == '*':
        return True
    if i == -1 or j == -1:
        return False
    if cache[i][j]:
        return cache[i][j]
    if s[i] == r[j]:
        cache[i][j] = matche(i - 1, j - 1, s, r)
        return cache[i][j]
    elif r[j] == '.':
        cache[i][j] = matche(i - 1, j - 1, s, r)
        return cache[i][j]
    elif r[j] == '*':
        cache[i][j] = matche(i - 1, j, s, r) or matche(i, j - 1, s, r)
        return cache[i][j]
    return False


def matches_dp(s, r):
    M = len(s)
    N = len(r)
    dp = [[False for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0] = True
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if s[i - 1] == r[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif r[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif r[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[M][N]
