from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        count = 0
        total = 0
        cols = defaultdict(int)
        rows = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cols[j] += 1
                    rows[i] += 1
                    total += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if max(cols[j], rows[i]) == 1:
                        count += 1

        return total - count


if __name__ == '__main__':
    # arr = [[1, 0], [0, 1]]
    solution = Solution()
    # result = solution.countServers(arr)
    # print(result)

    # grid = [[1, 0], [1, 1]]
    # result = solution.countServers(grid)
    # print(result)
    #
    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    result = solution.countServers(grid)
    print(result)
