array = [1, 2, 3, 4, 5]
k = 3  # output = 4


def value_greater_k(nums, k):
    if not nums:
        return -1

    low = 0
    high = len(array) - 1

    if k < nums[low]:
        return low
    if k > nums[high]:
        return -1

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid - 1] < k < nums[mid]:
            return mid
        elif nums[mid] <= k < nums[mid + 1]:
            return mid + 1
        elif nums[mid] <= k:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    # array = [1, 1, 1, 1, 5]
    array = [1, 1, 2, 2]
    k = 2

    result = value_greater_k(array, k)
    print(result)
