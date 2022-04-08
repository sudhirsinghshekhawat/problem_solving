class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 1:
            return True
        elif n <= 9:
            return False
        square = self.square_sum(n)
        return self.isHappy(square)

    def square_sum(self, num):
        sum = 0
        while num:
            rem = num % 10
            sum += rem ** 2
            num = num // 10
        return sum


if __name__ == '__main__':
    num = 11
    s = Solution()
    print(s.isHappy(num))
