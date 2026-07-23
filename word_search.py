# Tags: backtracking, dfs, matrix, string
from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def isValidPos(pos: tuple[int, int]) -> bool:
            row, col = pos[0], pos[1]
            return row >= 0 and row < len(board) and col >= 0 and col < len(board[i])

        def dfs(pos: tuple[int, int], lastPosSet: Set[tuple[int, int]], k: int) -> bool:
            up = (pos[0] - 1, pos[1])
            down = (pos[0] + 1, pos[1])
            left = (pos[0], pos[1] - 1)
            right = (pos[0], pos[1] + 1)
            nextSteps = [up, down, left, right]
            for nextStep in nextSteps:
                if nextStep in lastPosSet:
                    continue
                if (
                    isValidPos(nextStep)
                    and board[nextStep[0]][nextStep[1]] == word[k]
                ):  
                    if k == len(word) - 1:
                        return True
                    else:
                        if dfs(nextStep, lastPosSet | {pos}, k + 1):
                            return True
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    if dfs((i, j), set(), 1):
                        return True

        return False


if "__main__" == __name__:
    sol = Solution()
    print(
        sol.exist(
            board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
            word="ABCESEEEFS",
        )
    )
