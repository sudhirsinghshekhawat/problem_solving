from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        start = 0

        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total = total + tank
                tank = 0
        if (tank + total) < 0:
            return -1
        else:
            return start


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(s.canCompleteCircuit(gas, cost))
