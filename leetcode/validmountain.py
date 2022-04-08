array_1 = [0, 3, 4, 5, 6.3, 1]  # True
array_2 = [0, 3, 4, 4, 3, 5, 2]  # False


def valid_mountain(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1

    if 0 < left == right < n - 1:
        return True
    return False


if __name__ == '__main__':
    result = valid_mountain(array_1)
    print(result)

    result = valid_mountain(array_2)
    print(result)
