from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        n = len(matrix[0])
        j = n-1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    # val = [[1, 2]]
    s = Solution()
    # result = s.searchMatrix(val, 2)
    # print(result)
    #
    # val = [[1]]
    # result = s.searchMatrix(val, 1)
    # print(result)

    val = [[1, 1]]
    result = s.searchMatrix(val, 2)
    print(result)
