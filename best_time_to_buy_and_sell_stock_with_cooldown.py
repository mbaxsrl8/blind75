# Tags: dynamic-programming, needs-review
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_from_day = [0] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            best_buy_today = 0
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit <= 0:
                    continue
                best_buy_today = max(best_buy_today, best_from_day[j + 2] + profit if j + 2 < len(prices) else profit)
            best_from_day[i] = max(best_from_day[i + 1], best_buy_today)
        return best_from_day[0]        
        
    # def maxProfit(self, prices: list[int]) -> int:
    #     def makeTransaction(i: int) -> int:
    #         result = 0
    #         if i >= len(prices) - 1:
    #             return result
    #         for buy in range(i, len(prices) - 1):
    #             for sell in range(buy + 1, len(prices)):
    #                 if prices[sell] <= prices[buy]:
    #                     continue
    #                 profit = prices[sell] - prices[buy]
    #                 result = max(result, profit + makeTransaction(sell + 2))
    #         return result
                    
    #     return makeTransaction(0)            

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices=[1,3,4,0,4]))
