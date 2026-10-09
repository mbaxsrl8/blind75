# Tags: 2-d-dynamic-programming, string
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1) + 1, len(word2) + 1
        if rows == 0:
            return cols
        if cols == 0:
            return rows
        maxVal = rows + cols
        dp = [[maxVal for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            dp[r][0] = r
        for c in range(cols):
            dp[0][c] = c
        
        for r in range(1, rows):
            for c in range(1, cols):   
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = min(dp[r][c], dp[r-1][c-1])
                
        return dp[-1][-1]
            
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance(word1 = "horse", word2 = "ros"))