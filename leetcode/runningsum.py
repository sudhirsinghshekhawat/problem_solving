from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array = []
        sum_array.append(nums[0])
        for i in range(1, len(nums)):
            sum_array[i] += sum_array[i - 1]
        return sum_array


if __name__ == '__main__':
    # s = Solution()
    # nums = [1, 2, 3, 4]
    # result = s.runningSum(nums)
    # print(result)
    name = "sudhir singh"
    print(name.split())
