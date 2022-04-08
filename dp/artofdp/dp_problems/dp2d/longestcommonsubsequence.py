def lcs(i, j, A, B):
    if i == -1 or j == -1:
        return 0
    if A[i] == B[j]:
        return lcs(i - 1, j - 1, A, B) + 1
    else:
        return max(lcs(i - 1, j, A, B), lcs(i, j - 1, A, B))


def lcs_memo(i, j, A, B, cache):
    if i == -1 or j == -1:
        return 0
    if cache[i][j] == -1:
        return cache[i][j]
    if A[i] == B[j]:
        cache[i][j] = lcs_memo(i - 1, j - 1, A, B) + 1
    else:
        cache[i][j] = max(lcs_memo(i - 1, j, A, B), lcs_memo(i, j - 1, A, B))
    return cache[i][j]


def lcs_dp(A, B):
    m = len(A)
    n = len(B)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
