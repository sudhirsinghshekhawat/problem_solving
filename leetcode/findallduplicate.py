from typing import List

from _pytest.fixtures import fixture


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        result = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if nums_dict[num] > 1:
                result.append(num)
        return result

    def findDuplicates_1(self, nums: List[int]) -> List[int]:
        max_number = max(nums)
        nums_arr = [-1 for _ in range(max_number + 1)]
        result = []
        for num in nums:
            nums_arr[num] += 1
            if nums_arr[num] > 0:
                result.append(num)
        return result

    def find_duplicates(self, nums: List[int]) -> int:
        unique_numbers = set()
        for num in nums:
            if num in unique_numbers:
                return num
            unique_numbers.add(num)


class TestSolutions:

    @fixture
    def nums(self):
        return [1, 2, 3, 4, 3]

    @fixture
    def solution(self):
        return Solution()

    def test_find_duplicates(self, solution, nums):
        assert 3 == solution.find_duplicates(nums)


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    result = s.findDuplicates(nums)
    print(result)

    result_1 = s.findDuplicates_1(nums)
    print(result_1)
