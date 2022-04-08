# complexity O(nm)
# n is the length of target
# m is the length of pattern
def find_brute(target, pattern):
    n, m = len(target), len(pattern)
    for i in range(n - m + 1):
        k = 0
        while k < m and target[i + k] == pattern[k]:
            k += 1
        if k == m:
            return i
    return -1


# complexity O(m+n)
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
            i += (m - min(m, j + 1))
            k = m - 1
    return -1


def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail


# Complexity O(m+n)
def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1


if __name__ == '__main__':
    target = "sudhirsinghshekhawat"
    pattern = "singh"
    result = find_brute(target, pattern)
    print(result)

    target = "suds"
    pattern = "ud"

    result = find_boyer_moore(target, pattern)
    print(result)

    result = find_kmp(target, pattern)
    print(result)

    s1 = "sudhirsinghshekhawat"
    s2 = "singh"
    result = s1.find(s2)
    if result != -1:
        print(f"{s2} exist in {s1}")
    else:
        print(f"{s2} not exist in {s1}")

    print(f"index of {s2} is {s1.index(s2)}")
