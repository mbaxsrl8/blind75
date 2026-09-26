# Tags: dynamic-programming, 2-d-dynamic-programming, needs-review
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for target in range(coin, len(dp)):
                dp[target] += dp[target - coin]
        
        return dp[-1]
        
        
    # def change(self, amount: int, coins: list[int]) -> int:
    #     coins = sorted(coins)
    #     def backtrack(index: int, target: int) -> int:
    #         if target == 0:
    #             return 1
    #         result = 0
    #         for i in range(index, len(coins)):
    #             if coins[i] > target:
    #                 break
    #             result += backtrack(i, target - coins[i])
    #         return result
    #     return backtrack(0, amount)


if __name__ == "__main__":
    sol = Solution()
    print(sol.change(amount=4, coins=[1, 2, 3]))
