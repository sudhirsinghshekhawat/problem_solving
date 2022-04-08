def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_1(n):
    a = 0
    b = 1
    c = 0
    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return c


def fib_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    n = 5
    fib_n = fib(6)
    print(fib_n)

    fib_n = fib_1(5)
    print(fib_n)

    fib_n = fib_dp(5)
    print(fib_n)
