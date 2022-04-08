def max_profit(i, s):
    if i < 0:
        return 0
    if i == 0:
        return s[0]
    return max(s[i] + max_profit(i - 2, s), max_profit(i - 1, s))


def max_profit_memo(i, s, cache):
    if i < 0:
        return 0
    if i == 0:
        return s[0]
    if cache[i] != 0:
        return cache[i]
    profit = max(s[i] + max_profit_memo(i - 2, s, cache), max_profit(i - 1, cache))
    cache[i] = profit
    return profit


def max_profit_dp(s):
    N = len(s)
    dp = [0 for _ in range(N + 1)]
    dp[1] = s[0]
    for i in range(2, N + 1):
        dp[i] = max(dp[i - 1], s[i - 1] + dp[i - 2])
    return dp[N]


def max_profit_dp_reconstruct(s):
    N = len(s)
    dp = [0 for _ in range(N + 1)]
    rob = [False for _ in range(N)]
    rob[0] = True
    dp[1] = s[0]

    for i in range(2, N + 1):
        if dp[i - 1] < s[i - 1] + dp[i - 2]:
            rob[i - 1] = True
            dp[i] = s[i - 1] + dp[i - 2]
        else:
            rob[i - 1] = False
            dp[i] = dp[i - 1]
    i = N - 1
    while i >= 0:
        if rob[i]:
            print("{} = {}".format(i, s[i]))
            i = i - 2
        else:
            i = i - 1
    return dp[N]


if __name__ == '__main__':
    money_arr = [20, 25, 30, 15, 10]
    len_arr = len(money_arr) - 1
    profit = max_profit(len_arr, money_arr)
    print(profit)

    cache = [0 for i in range(len(money_arr) + 1)]
    profit = max_profit_memo(len_arr, money_arr, cache)
    print(profit)

    profit = max_profit_dp(money_arr)
    print(profit)

    profit = max_profit_dp_reconstruct(money_arr)
    print(profit)
