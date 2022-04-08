def binarySearch(array, target):
    if not array:
        return -1
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    # result = binarySearch(arr, 5)
    # print(f"value 5 exist at index : {result}")
    # result = binarySearch(arr, 6)
    # print(f"value 6 exist at index : {result}")
    result = binarySearch(arr, 9)
    print(f"value  exist at index : {result}")
