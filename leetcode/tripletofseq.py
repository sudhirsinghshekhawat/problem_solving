import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small = sys.maxsize
        second_small = sys.maxsize
        for num in nums:
            if num <= first_small:
                first_small = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        return False
