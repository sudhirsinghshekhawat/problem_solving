from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans, i = [], 0
        while i < len(nums):
            lower = upper = nums[i]
            while i < len(nums) and nums[i] == upper:
                i += 1
                upper += 1
            ans.append(str(lower) + ("->" + str(upper - 1) if upper - lower - 1 else ""))
        return ans


if __name__ == '__main__':
    arr = [0, 1, 2, 4, 5, 7]
    solution = Solution()
    result = solution.summaryRanges(arr)
    print(result)
