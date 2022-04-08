from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)

        count_dict = defaultdict(int)
        max_count = 0

        for num in nums:
            count_dict[num] += 1
            if count_dict[num] > max_count:
                max_count = count_dict[num]
            if max_count > n // 2:
                return num

        return -1

    def majority_element_2(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0

        for num in nums:
            if votes == 0:
                candidate = num
                votes += 1
            else:
                if num == candidate:
                    votes += 1
                else:
                    votes -= 1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate

        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 3]
    result = solution.majorityElement(nums)
    print(result)

    nums = [2, 2, 1, 1, 1, 2, 2]
    result = solution.majorityElement(nums)
    print(result)

    result = solution.majority_element_2(nums)
    print(result)
