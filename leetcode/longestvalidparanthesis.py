class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        stack = [-1]
        result = 0

        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])

        return result


class TestSolution:

    def setup(self):
        self.solution = Solution()

    def test_longest_valid_parenthesis(self):
        s = "(()"
        assert 2 == self.solution.longest_valid_parentheses(s)
