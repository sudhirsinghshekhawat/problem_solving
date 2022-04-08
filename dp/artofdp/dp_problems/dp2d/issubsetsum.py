def is_subset_sum(numbers, n, target_sum):
    if target_sum == 0:
        return True

    if n == 0:
        return False

    if numbers[n - 1] > target_sum:
        return is_subset_sum(numbers, n - 1, target_sum)

    return is_subset_sum(numbers, n - 1, target_sum) or is_subset_sum(numbers, n - 1, target_sum - numbers[n - 1])


def is_subset_sum_cache(numbers, n, target_sum, cache):
    if target_sum == 0:
        return True

    if n == 0:
        return False

    if cache[n][target_sum] != -1:
        return cache[n][target_sum]

    if numbers[n - 1] > target_sum:
        cache[n][target_sum] = is_subset_sum_cache(numbers, n - 1, target_sum, cache)

    exclusion = is_subset_sum_cache(numbers, n - 1, target_sum, cache)
    inclusion = is_subset_sum_cache(numbers, n - 1, target_sum - numbers[n - 1], cache)

    cache[n][target_sum] = exclusion or inclusion

    return cache[n][target_sum]


def is_subset_sum_dp(numbers, n, target_sum):
    cache = [[-1 for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(target_sum):
            if i == 0:
                cache[i][j] = False
            if j == 0:
                cache[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if numbers[i - 1] > j:
                cache[i][j] = cache[i - 1][j]
            else:
                cache[i][j] = cache[i - 1][j] or cache[i - 1][j - numbers[i - 1]]

    return cache[n - 1][target_sum - 1]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
target_sum = 24

cache = [[-1 for _ in range(target_sum + 1)] for _ in range(n + 1)]
print(f"Answer : {is_subset_sum_cache(numbers, n, target_sum, cache)}")
print(f"Answer : {is_subset_sum_dp(numbers, n, target_sum)}")
