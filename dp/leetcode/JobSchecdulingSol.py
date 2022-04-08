import bisect


class Solution:
    ...


l = [1, 2, 3, 4, 5, 6, 8, 9]
print(bisect.bisect_left(l, 7, 0))
print(bisect.bisect_right(l, 7))
