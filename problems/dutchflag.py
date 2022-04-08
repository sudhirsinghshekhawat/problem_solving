arr = [11, 2, 9, 10, 13, 17, 21]


def arrange_arr_1(array, target):
    output = [target for _ in range(len(array))]
    i, j = 0, len(array) - 1
    for k in range(len(array)):
        if array[k] < target:
            output[i] = array[k]
            i += 1
        elif array[k] > target:
            output[j] = array[k]
            j -= 1
    return output


def solve(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        while nums[i] < target:
            i += 1
        while nums[j] > target:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]


result = arrange_arr_1(arr, 10)
print(result)

solve(arr, 10)
print(arr)
