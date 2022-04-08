from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        numbers_dict = {0: -1}
        max_len = 0
        count = 0

        for i, num in enumerate(nums):
            count = count + (1 if num == 1 else -1)
            if count in numbers_dict:
                max_len = max(max_len, i - numbers_dict[count])
            else:
                numbers_dict[count] = i
        return max_len


if __name__ == '__main__':
    array = [0, 1, 0, 0, 1, 0, 1]
    solution = Solution()
    result = solution.findMaxLength(array)
    print(result)
