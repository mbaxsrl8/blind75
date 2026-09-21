# Tags: breadth-first-search, matrix, review-priority
# You are given a m×n m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]):
        INF = 2147483647
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque(
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c] == 0
        )

        while queue:
            r, c = queue.popleft()
            for move in next_moves:
                nr = r + move[0]
                nc = c + move[1]
                if 0<=nr<rows and 0 <=nc<cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
                


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    sol.islandsAndTreasure(grid)
    print(grid)
