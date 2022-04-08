def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
                   knapsack(W, wt, val, n - 1))


def knapsack_dp(W, wt, val, n):
    k = [[0 for i in range(W + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i - 1] <= w:
                k[i][w] = max(val[i - 1] + k[i - 1][W - wt[i - 1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]
    return k[n][w]


def main():
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))
    print(knapsack_dp(W, wt, val, n))


if __name__ == '__main__':
    main()
