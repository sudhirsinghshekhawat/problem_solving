from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for s in strs:
            ones = s.count("1")
            zeros = s.count("0")

            for i in range(n, ones-1, -1):
                for j in range(m, zeros-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros]+1)
        return dp[n][m]

if __name__ == '__main__':
    strs = ["10","0","1"]
    m = 1
    n = 1
    solution = Solution()
    result = solution.findMaxForm(strs,m,n)
    print(result)