# Tags: matrix, review-priority

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        rows,cols = len(matrix), len(matrix[0])
        for i in range((min(rows,cols)+1)//2):
            bottom = rows - i
            right = cols - i
            for c in range(i, right):
                res.append(matrix[i][c])
            for r in range(i+1, bottom):
                res.append(matrix[r][right-1])
            if i != bottom-1:
                for c in range(right-2, i-1, -1):
                    res.append(matrix[bottom-1][c])
            if i != right -1:
                for r in range(bottom-2, i, -1):
                    res.append(matrix[r][i])

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
