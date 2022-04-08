import collections
from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.arr = []
        count = collections.Counter()
        leader = None
        m = 0

        for p, t in zip(persons, times):
            count[p] += 1
            c = count[p]

            if c >= m:
                if p != leader:
                    leader = p
                    self.arr.append((p, t))
            if c > m:
                m = c

    def q(self, t: int):
        low = 1
        high = len(self.arr)

        while low < high:
            mid = low + (high - low) // 2
            if self.arr[mid][1] <= t:
                low = mid + 1
            else:
                high = mid
        return self.arr[low - 1][0]


if __name__ == '__main__':
    ...
