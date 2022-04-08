import collections
from typing import List


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:
                deque.pop()
            if deque and (i - deque[0]) >= k:
                deque.popleft()
            deque.append(i)
            res.append(nums[deque[0]])
        return res[k - 1:]


if __name__ == '__main__':
    s = Solution()
    arr = [4, -1, 2, 2, 5, 6, 8, 7, 8, 9, 10]
    result = s.max_sliding_window(arr, 3)
    print(result)
