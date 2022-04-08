def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while left_idx <= right_idx:
        if array[right_idx] < array[pivot_idx] < array[left_idx]:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    array[pivot_idx], array[right_idx] = array[right_idx], array[pivot_idx]
    quick_sort_helper(array, start_idx, right_idx - 1)
    quick_sort_helper(array, right_idx + 1, end_idx)


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    result = quick_sort(array)
    print(result)
