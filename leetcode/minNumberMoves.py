from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def min_no_moves(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        moves_count = 0
        nums.sort()

        while left < right:
            moves_count += nums[right] - nums[left]
            left += 1
            right -= 1

        return moves_count


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input_list,output", [([1, 2, 3], 2), ([1, 10, 2, 9], 16)])
    def test_min_no_moves(self, solution, input_list, output):
        assert output == solution.min_no_moves(input_list)
