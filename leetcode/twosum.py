from typing import List

import pytest


class Solution:


    """
    2 sum problem for array is sorted
    """


def two_sum(self, numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers) - 1

    while low < high:
        sum = numbers[low] + numbers[high]
        if sum == target:
            return [low + 1, high + 1]
        elif sum < target:
            low += 1
        else:
            high -= 1

    return [-1, -1]


class TestSolution:

    @pytest.mark.parametrize("arr,target,output", [([2, 7, 11, 15], 9, [1, 2]),
                                                   ([2, 7, 11, 15], 16, [-1, -1])])
    def test_two_sum(self, arr, target, output):
        solution = Solution()
        assert output == solution.two_sum(arr, target)
