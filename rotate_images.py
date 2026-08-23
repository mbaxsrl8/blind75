# Tags: matrix

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for r in range(0, n//2):
            for c in range(r, n - 1-r):
                posList = [(r,c), (c, n-1-r), (n-1-r, n-1-c), (n-1-c, r)]
                print('posList for {} is {}'.format((r,c), posList))
                v = matrix[r][c]
                for i in range(1, 4):
                    pos = posList[i]
                    tmp = matrix[pos[0]][pos[1]]
                    matrix[pos[0]][pos[1]] = v
                    v =tmp
                matrix[r][c] = v

        print(matrix)


if __name__ == "__main__":
    sol = Solution()
    sol.rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
