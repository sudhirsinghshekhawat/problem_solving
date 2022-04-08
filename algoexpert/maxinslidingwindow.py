# time complexity = O(nk)
from collections import deque


def max_in_sliding_window_1(array, k):
    if not array:
        return []
    if len(array) < k:
        return [max(array)]

    result = []

    for i in range(len(array) - k + 1):
        max_in_array = array[i]
        for j in range(i, i + k):
            if array[j] > array[i]:
                max_in_array = array[j]
        result.append(max_in_array)
    return result


def max_in_sliding_window(array, k):
    deq = deque()
    result = []

    for i, num in enumerate(array):
        while deq and arr[deq[-1]] < num:
            deq.pop()
        if deq and i - deq[0] >= k:
            deq.popleft()
        deq.append(i)
        result.append(array[deq[0]])
    return result[k - 1:]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    result = max_in_sliding_window_1(arr, 3)
    print(f" Result : {result}")
    result = max_in_sliding_window(arr, 3)
    print(f" Result : {result}")
