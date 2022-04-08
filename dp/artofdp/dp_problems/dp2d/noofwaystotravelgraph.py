def no_of_ways_travel_graph(i, j):
    if i == 1 or j == 1:
        return 1
    return no_of_ways_travel_graph(i - 1, j) + no_of_ways_travel_graph(i, j - 1)


def no_of_ways_trvel_graph(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
