from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def pascal_triangle(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("number,result",
                             [(1, [[1]]), (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])])
    def test_pascal_triangle(self, solution, number, result):
        assert result == solution.pascal_triangle(number)
