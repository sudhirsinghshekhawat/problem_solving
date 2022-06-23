import heapq
from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def schedule_course(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        heapq.heapify(heap)
        time = 0

        for course in courses:
            if time + course[0] <= course[1]:
                time += course[0]
                heapq.heappush(heap, -1 * course[0])
            elif len(heap) != 0 and heap[0] * -1 > course[0]:
                time -= (-1 * heapq.heappop(heap))
                time += course[0]
                heapq.heappush(heap, -1 * course[0])

        return len(heap)


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input,output", [([[1, 2]], 1), ([[3, 2], [4, 3]], 0)])
    def test_schedule_course(self, solution, input, output):
        assert output == solution.schedule_course(input)
