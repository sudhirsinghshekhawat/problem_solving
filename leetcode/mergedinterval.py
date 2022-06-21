"""
test cases:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

"""
from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def merge_interval(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


class TestSolution:

    @pytest.mark.parametrize("input,output", [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]), (
            [[1, 4], [4, 5]], [[1, 5]])])
    def test_merge_interval(self, input, output):
        solution = Solution()
        assert output == solution.merge_interval(input)
