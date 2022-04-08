def find_brute(T, P):
    """
    finding sub string exist or not in brute force way
    and complexity is O(mn)
    """
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m - 1
    k = m - 1

    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
            print(sep='')
    return -1


if __name__ == '__main__':
    # T = "abacaabaccabacabaabb"
    # P = "abacab"
    # print(find_brute(T, P))

    T = "sudhir"
    P = "udh"
    find_boyer_moore(T, P)
