def find_flips(string, n):
    last = ' '
    res = 0
    for i in range(n):
        if last != string[i]:
            res += 1
        last = string[i]
    return res // 2


if __name__ == '__main__':
    str = '0001111000111100'
    n = len(str)
    print(find_flips(str, n))
