# Tags: dynamic-programming, review-priority

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
        
    def coinChange2(self, coins: List[int], amount: int) -> int:
        res = -1
        coins = sorted(coins, reverse=True)
        def calc(available_coins: List[int], remain:int, pre: int):
            nonlocal res
            if res != -1 and pre >= res:
                return
            if remain == 0:
                res = min(res, pre) if res != - 1 else pre
            
            for coin in available_coins:
                if coin <= remain:
                    calc(available_coins, remain- coin, pre+1)
        
        for i in range(len(coins)):
            calc(available_coins=coins[i:], remain=amount, pre=0)
        return res
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.coinChange([1], 0))
