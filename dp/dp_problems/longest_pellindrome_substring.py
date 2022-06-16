import pytest
from _pytest.fixtures import fixture


class Solution:

    def __init__(self):
        self.result_start = 0
        self.result_length = 0

    def longest_palindrome_sub_string(self, string: str):
        str_length = len(string)
        if str_length < 2:
            return string
        for start in range(str_length):
            self.expand_range(string, start, start)
            self.expand_range(string, start, start + 1)
        return string[self.result_start: self.result_start + self.result_length]

    def expand_range(self, string, start, end):
        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1

        if self.result_length < (end - start - 1):
            self.result_start = start + 1
            self.result_length = end - start - 1


class TestSolution:

    @fixture
    def solution_object(self):
        solution = Solution()
        return solution

    @pytest.mark.parametrize("input,output", [("babad", "bab"), ("cbbd", "bb")])
    def test_longest_palindrome_sub_string(self, input, output, solution_object):
        assert output == solution_object.longest_palindrome_sub_string(input)
