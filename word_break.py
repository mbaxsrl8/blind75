# Tags: dynamic-programming, string
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp.append(True)
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(s) - i < len(word):
                    continue
                if s[i:i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
    
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     ## brute force
    #     return self.recursive(s, wordDict, 0)

    # def recursive(self, s: str, wordDict: List[str], i) -> bool:
    #     if i == len(s):
    #         return True
    #     res = False
    #     for word in wordDict:
    #         if len(s) - i + 1 < len(word):
    #             continue
    #         if s[i:i+len(word)] == word:
    #             res |= self.recursive(s, wordDict, i + len(word))
    #     return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.wordBreak("catsincars", ["cats","cat","sin","in","car"]))
