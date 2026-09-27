# Tags: dynamic-programming, 2-d-dynamic-programming, needs-review
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 0: holding 1: not holding
        dp = [[0 for i in range(2)] for i in range(len(prices))]
        dp[-1][0] = prices[-1]
        for day in range(len(prices) - 2, -1, -1):
            for state in range(2):
                if state == 0: # holding stock
                    sell = prices[day]
                    if day + 2 < len(prices):
                        sell += dp[day + 2][1]
                    dp[day][0] = max(dp[day + 1][0], sell) # skip or sell
                else: # not holding stock
                    dp[day][1] = max(dp[day + 1][1], -prices[day] + dp[day + 1][0]) # skip or buy
        return dp[0][1]
                    
    
    # def maxProfit(self, prices: list[int]) -> int:
    #     dp = [0] * len(prices)
    #     for i in range(len(prices) - 2, -1, -1):
    #         dp[i] = dp[i + 1]
    #         for j in range(i + 1, len(prices)):
    #             if prices[j] > prices[i]:
    #                 profit = prices[j] - prices[i]
    #                 dp[i] = max(dp[i], profit + dp[j + 2] if j + 2 < len(dp) else profit)
    #     return dp[0]               

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices=[1,3,4,0,4]))
