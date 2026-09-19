# Tags: backtracking
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        path = []

        def backtrack(index: int):
            if index == n:
                subRes = []
                for co in path:
                    subRes.append("." * co + "Q" + "." * (n - co - 1))
                result.append(subRes)
                return
            for i in range(0, n):
                valid = True
                for r, col in enumerate(path):
                    if i == col:
                        valid = False
                        break
                    if abs(i - col) == abs(index - r):
                        valid = False
                        break
                if not valid:
                    continue

                path.append(i)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
