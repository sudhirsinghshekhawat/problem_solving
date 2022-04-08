def lis(i, a):
    if i == 0:
        return 1
    max_l = 1
    for j in range(i):
        l = lis(j, a)
        if a[j] < a[i]:
            l += 1
        max_l = max(max_l, l)
    return max_l


def lis_memo(i, a, cache):
    if i == 0:
        return 1
    if cache[i] != 0:
        return cache[i]
    max_l = 1
    for j in range(i):
        l = lis_memo(j, a, cache)
        if a[j] < a[i]:
            l += 1
        max_l = max(max_l, l)
    cache[i] = max_l
    return cache[i]


def lis_dp(arr):
    n = len(arr)
    dp = [1 for _ in range(len(arr))]
    for i in range(1, n):
        for j in range(i):
            # if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n - 1]


if __name__ == '__main__':
    arr = [5, 2, 3, 6, 8]
    print(lis(len(arr) - 1, arr))

    cache = [0 for _ in range(len(arr))]
    print(lis_memo(len(arr) - 1, arr, cache))

    print(lis_dp(arr))
