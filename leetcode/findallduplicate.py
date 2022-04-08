from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        result = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if nums_dict[num] > 1:
                result.append(num)
        return result

    def findDuplicates_1(self, nums: List[int]) -> List[int]:
        max_number = max(nums)
        nums_arr = [-1 for _ in range(max_number + 1)]
        result = []
        for num in nums:
            nums_arr[num] += 1
            if nums_arr[num] > 0:
                result.append(num)
        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    result = s.findDuplicates(nums)
    print(result)

    result_1 = s.findDuplicates_1(nums)
    print(result_1)
