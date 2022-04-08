def f(n):
    sum = 0
    if n == 0 or n == 1:
        return 2
    for i in range(1, n):
        sum += 2 * f(i) * f(i - 1)
    return sum


def f_dp(n):
    T = [0] * (n + 1)
    T[0] = T[1] = 2
    for i in range(2, n + 1):
        T[i] = 0
        for j in range(1, i):
            T[i] += 2 * T[j] * T[j - 1]
    return T[n]


def main():
    print(f(4))
    print(f_dp(4))


if __name__ == '__main__':
    main()
