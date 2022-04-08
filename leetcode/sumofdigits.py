from leetcode.anagram import solution


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

if __name__ == '__main__':
    solution = Solution()
    result = solution.addDigits(123)
    print(result)

    result = solution.addDigits(38)
    print(result)
