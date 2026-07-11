# Tags: dynamic-programming, fibonacci

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n - 1]


if "__main__" == __name__:
    sol = Solution()
    print(sol.climbStairs(3))
