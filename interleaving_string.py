# Tags: dynamic-programming, 2-d-dynamic-programming, string, needs-review
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        dp = [[False for i in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[0][0] = True
        for i in range(len(s2) + 1):
            for j in range(len(s1) + 1):
                k = i + j - 1
                if k < 0:
                    continue
                if j - 1 >= 0 and s1[j - 1] == s3[k]:
                    dp[i][j] |= dp[i][j - 1]
                if i - 1 >= 0 and s2[i - 1] == s3[k]:
                    dp[i][j] |= dp[i - 1][j]

        return dp[-1][-1]

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False

    #     @cache
    #     def backtrack(i: int, j: int) -> bool:
    #         k = i + j
    #         if k == len(s3):
    #             return True
    #         if i < len(s1) and s1[i] == s3[k]:
    #             if backtrack(i + 1, j):
    #                 return True
    #         if j < len(s2) and s2[j] == s3[k]:
    #             if backtrack(i, j+1):
    #                 return True
    #         return False

    #     return backtrack(0, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave(s1 = "db", s2 = "b", s3 = "cbb"))
