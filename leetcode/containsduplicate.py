def contains_duplicate(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False


def contains_duplicate_1(arr):
    return not len(arr) == len(set(arr))
