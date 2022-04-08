def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# bottom up
def fibo_dp1(n):
    fib_table = [0, 1]
    for _ in range(2, n + 1):
        fib_table.append(fib_table[_ - 1] + fib_table[_ - 2])
    return fib_table[n]


# top down
fib_table = {0: 1, 1: 1}


def fib_dp2(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n in fib_table:
        return fib_table[n]
    else:
        fib_table[n] = fib_dp2(n - 1) + fib_dp2(n - 2)
        return fib_table[n]


def main():
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))
    print('------')
    print(fibo_dp1(4))
    print(fibo_dp1(5))
    print(fibo_dp1(6))
    print(fibo_dp1(7))
    print('------')
    print(fib_dp2(4))
    print(fib_dp2(5))
    print(fib_dp2(6))
    print(fib_dp2(7))
    print('------')
    print(fibo(4))
    print(fibo(5))
    print(fibo(6))
    print(fibo(7))


if __name__ == '__main__':
    main()
