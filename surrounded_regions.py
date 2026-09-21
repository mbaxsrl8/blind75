# Tags: matrix, breadth-first-search
from collections import deque

class Solution:
    def solve(self, board: list[list[str]]):
        rows, cols = len(board), len(board[0])
        queue = deque(
            (r, c)
            for r in range(rows)
            for c in range(cols)
            if board[r][c] == 'O' and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1)
        )
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            board[r][c] = '0'
            for move in next_moves:
                nr = r + move[0]
                nc = c + move[1]
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '0':
                    board[r][c] = 'O'
                    
        


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    sol.solve(board)
    print(board)
