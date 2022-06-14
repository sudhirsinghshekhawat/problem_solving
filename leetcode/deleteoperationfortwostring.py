import pytest


class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    continue
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return len(word1) + len(word2) - 2 * dp[-1][-1]


class TestSolution:

    @pytest.mark.parametrize("word1,word2,output", [("sea", "eat", 2), ("leetcode", "etco", 4)])
    def test_min_distance(self, word1, word2, output):
        solution = Solution()
        assert output == solution.min_distance(word1, word2)
