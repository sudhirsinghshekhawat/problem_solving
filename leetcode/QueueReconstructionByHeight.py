"""
Test case:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
"""
from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []

        for p in people:
            output.insert(p[1], p)

        return output


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input,output", [
        ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
        ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]], [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]])])
    def test_reconstruct_queue(self, solution, input, output):
        assert output == solution.reconstruct_queue(input)
