from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        min_purchase_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_purchase_price)
            min_purchase_price = min(min_purchase_price, price)
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    arr = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(arr)
    print(result)
