# Tags: array, two-pointers, sliding-window

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                sell = sell + 1
                if profit > max_profit:
                    max_profit = profit
            else:
                buy = buy + 1
                if sell == buy:
                    sell = sell + 1
        return max_profit
    

if '__main__' == __name__:
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))