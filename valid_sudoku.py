# Tags: hash-map, matrix

# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool: 
        for row in range(9):
            cache = set()
            for col in range(9):
                v = board[row][col]
                if v == '.':
                    continue
                v = int(v)
                if v in cache:
                    return False
                if v < 1 or v > 9:
                    return False
                cache.add(v)
            
        for col in range(9):
            cache = set()
            for row in range(9):
                v = board[row][col]
                if v == '.':
                    continue
                v = int(v)
                if v in cache:
                    return False
                if v < 1 or v > 9:
                    return False
                cache.add(v)
        
        for i in range(9):
            first_row = i // 3 * 3
            first_col = i % 3 * 3
            cache = set()
            for r in range(first_row, first_row + 3):
                for c in range(first_col, first_col + 3):
                    v = board[r][c]
                    if v == '.':
                        continue
                    v = int(v)
                    if v in cache:
                        return False
                    if v < 1 or v > 9:
                        return False
                    cache.add(v)

        return True
    
if '__main__' == __name__:
    sol = Solution()
    print(sol.isValidSudoku(board=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]))
