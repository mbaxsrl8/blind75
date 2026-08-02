# Tags: matrix

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        r, c = 0, 0
        res = []
        round = 0
        direction = 0  # 0: right 1: down 2: left 3: up
        while len(res) < len(matrix) * len(matrix[0]):
            res.append(matrix[r][c])
            if direction == 0:
                if c == len(matrix[0]) - 1 - round:
                    r += 1
                    direction = 1
                else:
                    c += 1
            elif direction == 1:
                if r == len(matrix) - 1 - round:
                    c -= 1
                    direction = 2
                else:
                    r += 1
            elif direction == 2:
                if c == 0 + round:
                    r -= 1
                    direction = 3
                else:
                    c -= 1
            else:
                if r == 0 + round + 1:
                    round += 1
                    c += 1
                    direction = 0
                else:
                    r -= 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
