def lcs_length(X, Y):
    if not X or not Y:
        return ""
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x + lcs_length(m, n)
    else:
        return max(lcs_length(X, n), lcs_length(m, Y), key=len)


def lcs_length_dp(str1, str2):
    table = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    result = ""
    x, y = len(str1), len(str2)
    while x != 0 and y != 0:
        if table[x][y] == table[x - 1][y]:
            x -= 1
        elif table[x][y] == table[x][y - 1]:
            y -= 1
        else:
            assert str1[x - 1] == str2[y - 1]
            result = str1[x - 1] + result
            x -= 1
            y -= 1
    return result


def main():
    X = "ABCBDAB"
    Y = "BDCABA"
    print(lcs_length(X, Y))
    print(lcs_length_dp(X, Y))


if __name__ == '__main__':
    main()
