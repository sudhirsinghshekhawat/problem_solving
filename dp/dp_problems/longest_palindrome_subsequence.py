def max_num(x, y):
    if x > y:
        return x
    return y


def lps(seq, i, j):
    if i == j:
        return 1
    if seq[i] == seq[j] and i + 1 == j:
        return 2
    if seq[i] == seq[j]:
        return lps(seq, i + 1, j - 1) + 2

    return max_num(lps(seq, i, j - 1), lps(seq, i + 1, j))


def main():
    seq = "agbdba"
    n = len(seq)
    print(f'lps : {lps(seq, 0, n - 1)}')


if __name__ == '__main__':
    main()
