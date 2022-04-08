from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])
        if n * m != r * c:
            return nums
        else:
            l = []
            res = []
            for i in range(n):
                l.extend(nums[i])
            for i in range(r):
                res.append(l[i * c:i * c + c])
            return res


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    s = Solution()
    print(s.matrixReshape(mat, r, c))
