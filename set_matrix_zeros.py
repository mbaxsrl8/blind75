# Tags: matrix

# Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

# You must update the matrix in-place.

# Follow up: Could you solve it using O(1) space?

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows,cols = len(matrix), len(matrix[0])
        first_row = False
        first_column = False
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row = True
        for r in range(rows):
            if matrix[r][0] == 0:
                first_column = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for c in range(1, cols):
            if matrix[0][c] != 0:
                continue
            for r in range(1, rows):
                matrix[r][c] = 0

        for r in range(rows):
            if matrix[r][0] != 0:
                continue
            for c in range(1, cols):
                matrix[r][c] = 0
        
        if first_row:
            for c in range(cols):
                matrix[0][c] = 0
        if first_column:
            for r in range(rows):
                matrix[r][0] = 0    
            
                


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,0,5],[6,7,8]]
    sol.setZeroes(matrix)
    print(matrix)
