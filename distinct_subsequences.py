# Tags: dynamic-programming, 2-d-dynamic-programming
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(t), len(s)
        dp = [[0 for c in range(cols)] for r in range(rows)]
        dp[0] = [1 if s[c]==t[0] else 0 for c in range(cols)]
        for r in range(1, rows):
            pre = 0
            for c in range(cols):
                if s[c] == t[r]:
                    dp[r][c] = pre               
                pre += dp[r-1][c]
        return sum(dp[-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct(s = "caaat", t = "cat"))
