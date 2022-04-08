import sys


def sum_closet_to_zero(arr):
    n = len(arr)
    arr.sort()
    if n < 2:
        print(f'invalid')
        return
    l = 0
    r = n - 1
    min_left = 1
    min_right = n - 1
    min_sum = sys.maxsize
    while l < r:
        sum = arr[l] + arr[r]
        if abs(min_sum) > abs(sum):
            min_sum = sum
            min_left = l
            min_right = r
        if sum < 0:
            l = l + 1
        else:
            r = r - 1
    return arr[min_left], arr[min_right]


def find_element_in_rotated_array(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                mid = mid + 1
        else:
            if arr[mid] < target < arr[right]:
                left = mid + 1
            else:

                right = mid - 1


def separate_even_odd(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


def separate_0_1(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


def separate_0_1_2(arr):
    left = 0
    right = len(arr) - 1
    mid = 0
    while mid <= right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            left = left + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right = right - 1


def main():
    arr = [1, 2, 3, 4, 5, 7, 9, 10, 8]
    separate_even_odd(arr)
    print(arr)

    arr = [0, 1, 0, 1, 1, 1, 0, 0]
    separate_0_1(arr)
    print(arr)

    arr = [0, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0]
    separate_0_1_2(arr)
    print(arr)


if __name__ == '__main__':
    main()
