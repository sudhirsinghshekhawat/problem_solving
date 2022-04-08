RED = 0
BLUE = 1
GREEN = 2


def min_cost(cost, i, color):
    if i == len(cost):
        return 0
    if color == RED:
        cost_blue = min_cost(cost, i + 1, BLUE)
        cost_green = min_cost(cost, i + 1, GREEN)
        return cost[i][RED] + min(cost_blue, cost_green)
    if color == BLUE:
        cost_red = min_cost(cost, i + 1, RED)
        cost_green = min_cost(cost, i + 1, GREEN)
        return cost[i][BLUE] + min(cost_red, cost_green)
    if color == GREEN:
        cost_red = min_cost(cost, i + 1, RED)
        cost_blue = min_cost(cost, i + 1, BLUE)
        return cost[i][GREEN] + min(cost_red, cost_blue)


def min_cost_memo(cost, i, color, cache):
    if i == len(cost):
        return 0
    if cache[i][color] != -1:
        return cache[i][color]
    if color == RED:
        cost_blue = min_cost(cost, i + 1, BLUE)
        cost_green = min_cost(cost, i + 1, GREEN)
        cache[i][RED] = cost[i][RED] + min(cost_blue, cost_green)
        return cache[i][RED]
    if color == BLUE:
        cost_red = min_cost(cost, i + 1, RED)
        cost_green = min_cost(cost, i + 1, GREEN)
        cache[i][BLUE] = cost[i][BLUE] + min(cost_red, cost_green)
        return cache[i][BLUE]
    if color == GREEN:
        cost_red = min_cost(cost, i + 1, RED)
        cost_blue = min_cost(cost, i + 1, BLUE)
        cache[i][GREEN] = cost[i][GREEN] + min(cost_red, cost_blue)
        return cache[i][GREEN]


def min_cost_dp(costs):
    n = len(costs)
    dp = [[0 for _ in range(3)] for _ in range(4)]
    print(dp)
    for i in range(1, n + 1):
        dp[i][RED] = costs[i - 1][RED] + min(dp[i - 1][BLUE], dp[i - 1][GREEN])
        dp[i][GREEN] = costs[i - 1][GREEN] + min(dp[i - 1][BLUE], dp[i - 1][RED])
        dp[i][BLUE] = costs[i - 1][BLUE] + min(dp[i - 1][GREEN], dp[i - 1][RED])
    return min(dp[n][RED], dp[n][BLUE], dp[n][GREEN])


if __name__ == '__main__':
    cost = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    cost_red = min_cost(cost, 0, RED)
    cost_blue = min_cost(cost, 0, BLUE)
    cost_green = min_cost(cost, 0, GREEN)
    min_cost_ = min(cost_red, cost_blue, cost_green)
    print(min_cost_)

    cache = [[-1 for _ in range(len(cost))] for _ in range(len(cost[0]))]
    cost_red = min_cost_memo(cost, 0, RED, cache)
    cost_blue = min_cost_memo(cost, 0, BLUE, cache)
    cost_green = min_cost_memo(cost, 0, GREEN, cache)
    min_cost_memo_ = min(cost_red, cost_blue, cost_green)
    print(min_cost_memo_)

    print(min_cost_dp(cost))
