from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0          # buy day
        max_profit = 0
        for r in range(1, len(prices)):  # sell day
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r  # found a lower buy price
        return max_profit

"""
Keep track of the minimum price seen so far while scanning prices.

For each day if its more than minimum, calculate profit = today’s price – min price so far.

Update max profit if this profit is greater.

Update min price if today’s price is lower.

"""



