# Tags: matrix

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for row in range(n // 2):
            for col in range((n + 1) // 2):
                (
                    matrix[col][n - 1 - row],
                    matrix[n - 1 - row][n - 1 - col],
                    matrix[n - 1 - col][row],
                    matrix[row][col],
                ) = (
                    matrix[row][col],
                    matrix[col][n - 1 - row],
                    matrix[n - 1 - row][n - 1 - col],
                    matrix[n - 1 - col][row],
                )

        print(matrix)


if __name__ == "__main__":
    sol = Solution()
    sol.rotate(matrix=[[1,2],[3,4]])
