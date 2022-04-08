def largest_range(array):
    best_range = []
    longest_length = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        current_length = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            left -= 1
            current_length += 1
        while right in nums:
            nums[right] = False
            right += 1
            current_length += 1
        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]
    return best_range


if __name__ == '__main__':
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    large_range = largest_range(array)
    print(large_range)
