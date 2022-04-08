from collections import deque


# O(n2)
def sliding_window_max(array, window):
    if not array:
        return None
    if len(array) < window:
        return max(array)

    result = []

    for i in range(len(array) - window + 1):
        max_in_array = array[i]
        for j in range(i, i + window):
            if array[j] > max_in_array:
                max_in_array = array[j]
        result.append(max_in_array)
    return result


# O(n)
def sliding_window_max_queue(array, window):
    max_array = []
    deq = deque()
    for i, num in enumerate(array):
        while deq and array[deq[-1]] < num:
            deq.pop()
        if deq and i - deq[0] >= window:
            deq.popleft()
        deq.append(i)
        max_array.append(array[deq[0]])
    return max_array[window - 1:]


if __name__ == '__main__':
    array = [3, 4, 5, 2, 6, 7, 4, 1, 2]
    result = sliding_window_max_queue(array, 3)
    print(result)
