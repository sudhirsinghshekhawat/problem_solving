from collections import defaultdict, Counter
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        res = [0] * k

        for ids, times in logs:
            d[ids].add(times)

        d = Counter(len(d[i]) for i in d)
        
        for i in d:
            res[i - 1] = d[i]

        return res


if __name__ == '__main__':
    solution = Solution()
    k = 5
    array = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    result = solution.findingUsersActiveMinutes(array, k)
    print(result)
