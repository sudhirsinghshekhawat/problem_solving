import sys

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def avg_of_5_elements_brute_force(arr, k=5):
    result = []
    for i in range(len(arr) - k + 1):
        sum = 0.0
        for j in range(i, i + k):
            sum += arr[j]
        result.append(sum / k)
    return result


def sum_of_avg_5_elements(arr, k=5):
    window_sum = 0
    window_start = 0
    result = []

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1
    return result


result = avg_of_5_elements_brute_force(arr, 5)
print(result)
result = sum_of_avg_5_elements(arr, 4)
print(result)


def max_sum_in_window(arr, k=3):
    max_sum = 0
    running_sum = 0
    window_start = 0
    max_sum_array = []

    for window_end in range(len(arr)):
        running_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, running_sum)
            max_sum_array.append(max_sum)
            running_sum -= arr[window_start]
            window_start += 1
    return max_sum_array


arr = [2, 1, 5, 1, 3, 2]
result = max_sum_in_window(arr, 3)
print(result)


def smallest_array_sum(arr, s):
    window_sum = 0
    min_length = sys.maxsize
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == sys.maxsize:
        return 0
    return min_length


arr = [2, 1, 5, 2, 3, 2]
result = smallest_array_sum(arr, 7)
print(result)
