"""
Input: nums = [100,4,200,1,3,2]
Output: 4

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input_list,output", [([100, 4, 200, 1, 3, 2], 4), ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)])
    def test_longest_consecutive_sequence(self, solution, input_list, output):
        assert output == solution.longest_consecutive_sequence(input_list)
