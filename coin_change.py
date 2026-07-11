# Tags: dynamic-programming, coin-change

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                elif coin == i:
                    dp[i] = 1
                dp[i] = min(dp[i - coin] + 1, dp[i])
        

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.coinChange([1], 0))