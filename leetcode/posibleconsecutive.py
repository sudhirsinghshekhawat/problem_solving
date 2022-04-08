import collections
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort()
        for n in keys:
            if count[n] > 0:
                minus = count[n]
                for i in range(n, n + k):
                    if count[i] < minus:
                        return False
                    count[i] -= minus
        return True


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4, 5, 6]
    k = 4
    solution = Solution()
    result = solution.isPossibleDivide(nums, k)
    print(result)
