from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        length = len(self.nums)
        if left < 0 or right < 0:
            return
        if left >= length or right >= length:
            return
        sum = 0
        while left < right:
            sum += self.nums[left] + self.nums[right]
            left += 1
            right -= 1
        return sum


if __name__ == '__main__':
    nums_array = [-2, 0, 3, -5, 2, -1]
    n = NumArray(nums_array)
    print(n.sumRange(2,5))
    
