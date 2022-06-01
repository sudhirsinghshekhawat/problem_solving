from typing import List


class Solution:

    def running_sum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n):
            nums[i] = nums[i - 1] + nums[i]

        return nums


class TestSolution:

    def setup(self):
        self.solution = Solution()

    def test_running_sum(self):
        nums = [1, 2, 3, 4]
        result = [1, 3, 6, 10]
        assert result == self.solution.running_sum(nums)
