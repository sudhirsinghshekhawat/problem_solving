from typing import List

import pytest
from _pytest.fixtures import fixture


class Solution:
    def squared_sorted_array(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        squared_array = [0 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            print(i)
            small_value = abs(nums[left])
            larger_value = abs(nums[right])

            if small_value > larger_value:
                squared_array[i] = small_value ** 2
                left += 1
            else:
                squared_array[i] = larger_value ** 2
                right -= 1

        return squared_array


class TestSolution:

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input_list,output_list",
                             [([-6, -4, -2, 1, 3, 5], [1, 4, 9, 16, 25, 36]), ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])])
    def test_squared_sorted_array(self, solution, input_list, output_list):
        assert output_list == solution.squared_sorted_array(input_list)
