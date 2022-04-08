def catalan_recursive(n):
    if n <= 0:
        return 1
    else:
        count = 0
        for i in range(n):
            count += catalan_recursive(i) * catalan_recursive(n - i - 1)
        return count


def catalan_dp(n):
    catalan = [1, 1] + [0] * n
    for i in range(2, n + 1):
        for j in range(n):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]


def main():
    print(catalan_recursive(3))
    print(catalan_dp(3))


if __name__ == '__main__':
    main()
