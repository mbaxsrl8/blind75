# Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

# You must update the matrix in-place.

# Follow up: Could you solve it using O(1) space?

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        for r in range(len(matrix)):
            if not any(matrix[r][c] == 0 for c in range(len(matrix[0]))):
                continue
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                   matrix[r][c] = 'M'
                else:
                    matrix[r][c] = 0

        for col in range(len(matrix[0])):
            if not any(matrix[r][col] == 'M' for r in range(len(matrix))):
                continue
            for r in range(len(matrix)):
                matrix[r][col] = 0
            
                


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    sol.setZeroes(matrix)
    print(matrix)