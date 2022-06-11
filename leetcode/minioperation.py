from math import inf
from typing import List

import pytest


class Solution:
    def min_operations(self, nums: List[int], x: int) -> int:
        current = sum(nums)
        left = 0
        n = len(nums)
        mini = inf

        for right in range(n):
            current -= nums[right]
            while current < x and left <= right:
                current += nums[left]
                left += 1

            if current == x:
                mini = min(mini, n - 1 - right + left)

        return mini if mini != inf else -1


class TestSolution:

    @pytest.mark.parametrize("input,x,output", [([1, 1, 4, 2, 3], 5, 2)])
    def test_min_operations(self, input, x, output):
        solution = Solution()
        assert output == solution.min_operations(input, x)
