import heapq
from typing import List

import pytest
from _pytest.fixtures import fixture

"""
test case:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution:
    def find_kth_largest(self, nums: List[int], k: int):
        return heapq.nlargest(k, nums)[-1]


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input,k,output", [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)])
    def test_find_kth_largest(self, solution, input, k, output):
        assert output == solution.find_kth_largest(input, k)
