from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        k = k % len(nums)
        # return nums[-k:] + nums[:-k]
        return nums[k + 1:] + nums[:k + 1]

    def rotate_1(self, nums: List[int], k: int):
        k = k % len(nums)
        return nums[-k:] + nums[:-k]

    def rotate_2(self, nums: List[int], k: int):
        arr[:] = nums
        arr[2] = 555

        for i in range(len(nums)):
            arr[(i + k) % len(nums)] = nums[i]
        nums[:] = arr
        return nums


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr = s.rotate(arr, 3)
    print(arr)

    arr_1 = [1, 2, 3, 4, 5, 6, 7]
    arr_1 = s.rotate_1(arr_1, 3)
    print(arr_1)

    arr_2 = [1, 2, 3, 4, 5, 6, 7]
    arr_2 = s.rotate_2(arr_2,3)
    print(arr_2)
