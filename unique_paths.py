# Tags: dp, matrix

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0 for _ in range(n)] for i in range(m)]
        dp[0][1] = 1
        dp[1][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(1, 2))
