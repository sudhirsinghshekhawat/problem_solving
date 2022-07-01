from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def max_unit_truck(self, box_types: List[List[int]], truck_size: int) -> int:
        box_types.sort(key=lambda row: row[1], reverse=True)
        units = 0

        for box in box_types:
            if truck_size > box[0]:
                units += (box[0] * box[1])
            elif truck_size > 0:
                units += (truck_size * box[1])
            truck_size -= box[0]

        return units


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("box_types,truck_size,output",
                             [([[1, 3], [2, 2], [3, 1]], 4, 8), ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91)])
    def test_max_unit_truck(self, solution, box_types, truck_size, output):
        assert output == solution.max_unit_truck(box_types, truck_size)
