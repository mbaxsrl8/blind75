# Tags: dynamic-programming, string
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## dynamic programming
        # dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     # brute force
    #     shorter_str = text1
    #     longer_str = text2
    #     if len(text2) < len(text1):
    #         shorter_str = text2
    #         longer_str = text1
    #     return self.recursive(shorter_str, longer_str, 0, -1)

    # def recursive(self, shorter_str: str, longer_str: str, i, min_pos) -> int:
    #     if i == len(shorter_str):
    #         return 0
    #     # find position in longer text
    #     char = shorter_str[i]
    #     pos = None
    #     for j in range(min_pos + 1, len(longer_str)):
    #         if longer_str[j] == char:
    #             pos = j
    #             break
    #     res1 = 0
    #     if pos is not None:
    #         res1 = self.recursive(shorter_str, longer_str, i + 1, pos) + 1
    #     res2 = self.recursive(shorter_str, longer_str, i + 1, min_pos)
    #     return max(res1, res2)


if "__main__" == __name__:
    sol = Solution()
    print(sol.longestCommonSubsequence("cat", "crabt"))
