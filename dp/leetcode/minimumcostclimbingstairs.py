# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
cost = [10, 15, 20]


def min_cost_climbing_stairs(cost):
    n = len(cost)
    return min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost(cost, n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return cost[n]
    return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost_climbing_stairs_memo(cost):
    n = len(cost)
    dp = [0 for _ in range(len(cost))]
    return min(min_cost(cost, n - 1), min_cost(cost, n - 2))


def min_cost_memo(cost, dp, n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return cost[n]
    if dp[n] != 0:
        return dp[n]
    result = cost[n] + min(min_cost_memo(cost, dp, n - 1), min_cost_memo(cost, dp, n - 2))
    dp[n] = result
    return dp[n]


def min_cost_dp(cost):
    n = len(cost)
    dp = [0 for _ in range(n)]
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])


result = min_cost_climbing_stairs(cost)
print(result)

result = min_cost_climbing_stairs_memo(cost)
print(result)

result = min_cost_dp(cost)
print(result)
