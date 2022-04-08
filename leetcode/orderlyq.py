from collections import deque


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if not s:
            return s
        if k > len(s) or k < 1:
            return s
        if len(s) == 2 or k == 1:
            s += s[0]
            s = s.replace(s[0], '', 1)
            return s
        s += s[0]
        s = s.replace(s[0], '', 1)
        s += s[k - 1]
        s = s.replace(s[k - 1], '', 1)
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.orderlyQueue("nhtq", 1))
