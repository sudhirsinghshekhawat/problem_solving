def find_repeated_number(arr):
    if not arr:
        return -1
    for i, val in enumerate(arr):
        index = abs(val)
        if arr[index] < 0:
            return index
        arr[index] = -arr[index]

    return -1


if __name__ == '__main__':
    arr = [4, 1, 3, 2, 5, 4, 5, 5]
    result = find_repeated_number(arr)
    print(result)
