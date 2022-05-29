from typing import List

import pytest


class Solution:
    def max_product(self, words: List[str]) -> int:

        def no_common_letter(s1, s2):
            for ch in s1:
                if ch in s2:
                    return False
            return True

        n = len(words)
        max_prod = 0

        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letter(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))

        return max_prod


class TestSolution:

    def setup(self):
        self.solution = Solution()

    @pytest.mark.parametrize("words,output", [(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
                                              (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
                                              (["a", "aa", "aaa", "aaaa"], 0)])
    def test_max_product(self, words, output):
        assert self.solution.max_product(words) == output
