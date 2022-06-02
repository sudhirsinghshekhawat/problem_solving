from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        ans = [[0 for _ in range(row)] for _ in range(col)]
        print(ans)
        for i in range(row):
            for j in range(col):
                ans[j][i] = matrix[i][j]
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    solution = Solution()
    result = solution.transpose(matrix)
    print(result)
