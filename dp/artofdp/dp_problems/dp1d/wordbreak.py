def count_ways(i, S, D):
    if i == -1:
        return 1
    count = 0
    for j in range(i, -1, -1):
        if S[j:i + 1] in D:
            count += count_ways(j - 1, S, D)
    return count


def count_ways_cache(i, S, D, cache):
    if i == -1:
        return 1
    if cache[i] != -1:
        return cache[i]
    count = 0
    for j in range(i, -1, -1):
        if S[j:i + 1] in D:
            count += count_ways_cache(j - 1, S, D, cache)
    cache[i] = count
    return count


def count_ways_dp(i, S, D):
    n = len(S)
    dp = [0 for _ in range(0, n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            if S[j - 1:i] in D:
                dp[i] += dp[j - 1]
    return dp[n]
