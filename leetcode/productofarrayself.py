from math import prod
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            nums_s = nums[:i] + nums[i + 1:]
            result.append(prod(nums_s))
        return result

    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            multiply_result = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                multiply_result *= nums[j]
            result.append(multiply_result)
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        output = []
        for i in nums:
            if i != 0:
                product = product * i
            else:
                if hasZero:
                    product = 0  # if two zeros are there entire list of output will be 0
                hasZero = True
        for i in nums:
            if i == 0:
                output.append(product)
            else:
                if hasZero:
                    output.append(0)
                else:
                    output.append(product // i)
        return output




if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    result = s.productExceptSelf_1(nums)
    print(result)
