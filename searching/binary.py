# recursive binary search
def binary_search(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            high = mid - 1
        if arr[mid] < k:
            low = mid + 1
    return -1


def binary_search_recursive(arr, k, low, high):
    mid = (high + low) // 2
    if low <= high:
        if arr[mid] == k:
            return mid
        if arr[mid] < k:
            return binary_search_recursive(arr, k, mid + 1, high)
        if arr[mid] > k:
            return binary_search_recursive(arr, k, low, mid - 1)
    else:
        return -1


def main():
    arr = [11, 21, 22, 25, 27, 29, 41, 42]
    index = binary_search(arr, 27)
    print(f'index of 27 is : {index}')
    index = binary_search(arr, 42)
    print(f'index of 42 is : {index}')
    index = binary_search(arr, 11)
    print(f'index of 11 is : {index}')
    index = binary_search(arr, 111)
    print(f'index of 111 is : {index}')

    index = binary_search_recursive(arr, 27, 0, len(arr) - 1)
    print(f'index of 27 is : {index}')
    index = binary_search_recursive(arr, 42, 0, len(arr) - 1)
    print(f'index of 41 is : {index}')
    index = binary_search_recursive(arr, 11, 0, len(arr) - 1)
    print(f'index of 11 is : {index}')
    index = binary_search_recursive(arr, 111, 0, len(arr) - 1)
    print(f'index of 111 is : {index}')


if __name__ == '__main__':
    main()
