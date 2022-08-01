import pytest
from _pytest.fixtures import fixture


class Solution:
    def unique_path(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("m,n,output", [(3, 7, 28), (3, 2, 3)])
    def test_unique_path(self, solution, m, n, output):
        assert output == solution.unique_path(m, n)
