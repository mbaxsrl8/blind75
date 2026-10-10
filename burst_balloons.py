# Tags: 2-d-dynamic-programming, needs-review
from functools import cache

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        ballons = [1] + nums + [1]
        @cache
        def calc(l:int, r: int) -> int:
            if l > r:
                return 0
            finalRes = 0
            for i in range(l, r + 1):
                coins = ballons[i] * ballons[l-1] * ballons[r + 1]
                coins += calc(l, i -1)
                coins += calc(i + 1, r)
                finalRes = max(finalRes, coins)
            return finalRes
        return calc(1, len(ballons) - 2)
                

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCoins(nums=[4, 2, 3, 7]))
