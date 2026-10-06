# Tags: dynamic-programming, depth-first-search, matrix
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for col in range(cols)] for row in range(rows)]
        longest = 0
        
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r: int, c: int):
            nonlocal longest
            if dp[r][c] != 0:
                return
            res = 1
            for next_move in next_moves:
                nr = r + next_move[0]
                nc = c + next_move[1]
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
                    dfs(nr, nc)
                    res = max(res, 1 + dp[nr][nc])
            dp[r][c] = res
            longest = max(longest, res)
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        
        return longest
                    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestIncreasingPath(matrix = [[5,5,3],[2,3,6],[1,1,1]]))
