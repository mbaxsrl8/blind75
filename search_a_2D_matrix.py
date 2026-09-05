# Tags: binary-search
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        cols = len(matrix[0])
        l,r = 0, len(matrix) * cols - 1
        if  target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while l < r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        row = l // cols
        col = l % cols
        return True if matrix[row][col] == target else False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
