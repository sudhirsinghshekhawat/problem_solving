arr = [1, 9, 6, 4, 5]


def inversion_count(arr):
    inversion = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversion += 1
    return inversion


def merge_sort(arr, n):
    temp_arr = [0] * n
    return _merge_sort(arr, temp_arr, 0, n - 1)


def _merge_sort(arr, temp_arr, left, right):
    inversion_count = 0

    if left < right:
        mid = (left + right) // 2
        inversion_count += _merge_sort(arr, temp_arr, left, mid)
        inversion_count += _merge_sort(arr, temp_arr, mid + 1, right)
        inversion_count += _merge(arr, temp_arr, left, mid, right)
    return inversion_count


def _merge(arr, temp_arr, left, mid, right):
    i = left
    k = left
    j = mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
            k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for _ in range(left, right + 1):
        arr[_] = temp_arr[_]

    return inv_count


print(inversion_count(arr))
print(merge_sort(arr, len(arr)))
