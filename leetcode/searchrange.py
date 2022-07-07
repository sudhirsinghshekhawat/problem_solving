"""
Leetcode : 34
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:

    def search_range(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.find_bind(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = self.find_bind(nums, target, False)
        return [lower_bound, upper_bound]

    def find_bind(self, nums: List[int], target: int, is_first: bool) -> int:
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                if is_first:
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums,target,output", [([5, 7, 7, 8, 8, 10], 8, [3, 4]),
                                                    # ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
                                                    ([], 0, [-1, -1])])
    def test_find_bind(self, solution, nums, target, output):
        assert output == solution.search_range(nums, target)
