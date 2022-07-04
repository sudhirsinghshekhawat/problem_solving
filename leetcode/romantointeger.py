import pytest
from _pytest.fixtures import fixture


class Solution:

    def __init__(self):
        self.values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def roman_to_integer(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and self.values[s[i + 1]] > self.values[s[i]]:
                total += self.values[s[i + 1]] - self.values[s[i]]
                i += 2
            else:
                total += self.values[s[i]]
                i += 1
        return total


class TestSolution:
    """
    input = "III"
    output = 3

    input = "LVIII"
    output = 58

    Input = "MCMXCIV"
    Output = 1994
    """

    @fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("input_str,output", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)])
    def test_roman_to_integer(self, solution, input_str, output):
        assert output == solution.roman_to_integer(input_str)
