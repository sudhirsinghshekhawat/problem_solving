def three_sum(arr, target):
    if len(arr) < 3:
        return []
    arr.sort()
    for i in range(len(arr)):
        remaining = target - arr[i]

        left = i + 1
        right = len(arr) - 1

        while left < right:
            if arr[left] + arr[right] == remaining:
                return [arr[i], arr[left], arr[right]]
            elif arr[left] + arr[right] < remaining:
                left += 1
            else:
                right -= 1

    return []


def three_sums(nums):
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    result = set()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        target = 0 - nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                result.add((nums[l], nums[r], nums[i]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(result)


if __name__ == '__main__':
    arr = [1, 4, 5, 2, 3, 7]
    three_elements = three_sum(arr, 12)
    print(three_elements)

    nums = [-1,0,1,2,-1,-4]
    three_elements = three_sums(nums)
    print(three_elements)
