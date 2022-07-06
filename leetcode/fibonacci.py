"""
Input: n = 2
Output: 1

Input: n = 3
Output: 2

Input: n = 4
Output: 3
"""
import pytest
from _pytest.fixtures import fixture


class Solution:

    def fibonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        cache = [0 for _ in range(n + 1)]
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("number,output", [(2, 1), (3, 2), (4, 3)])
    def test_fibonacci(self, solution, number, output):
        assert output == solution.fibonacci(number)
