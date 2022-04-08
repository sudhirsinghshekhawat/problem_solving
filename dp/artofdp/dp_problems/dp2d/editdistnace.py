def edit_distance(i, j, A, B):
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1
    if A[i] == B[j]:
        return edit_distance(i - 1, j - 1, A, B)
    else:
        return min(
            edit_distance(i, j - 1, A, B),
            edit_distance(i - 1, j - 1, A, B),
            edit_distance(i - 1, j, A, B)
        ) + 1


def edit_distance_memo(i, j, A, B, cache):
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1
    if cache[i][j] != -1:
        return cache[i][j]
    if A[i] == B[j]:
        distance = edit_distance_memo(i - 1, j - 1, A, B)
        cache[i][j] = distance
        return cache[i][j]
    else:
        distance = min(
            edit_distance_memo(i, j - 1, A, B),
            edit_distance_memo(i - 1, j - 1, A, B),
            edit_distance_memo(i - 1, j, A, B)
        ) + 1
        cache[i][j] = distance
        return cache[i][j]


def edit_distance_dp(A, B):
    M = len(A)
    N = len(B)
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    for i in range(M + 1):
        for j in range(N + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
    return dp[M][N]


if __name__ == '__main__':
    str1 = "abc"
    str2 = "yabd"

    result = edit_distance(len(str1) - 1, len(str2) - 1, str1, str2)
    print(result)
    result = edit_distance_dp(str1, str2)
    print(result)
