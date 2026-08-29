from typing import List, Optional, Set

from tree_node import TreeNode,convertListToTree


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)  + 1)
        dp[-1] = True
        shortest =21
        longest = 0
        for word in wordDict:
            shortest = min(shortest, len(word))
            longest = max(longest, len(word))
        
        r = len(s)-1
        while r >= shortest-1:
            for l in range(r-shortest + 1, r - longest, -1):
                for word in wordDict:
                    if word == s[l:r+1]:
                        dp[l] |= dp[r+1]
                        break
            r -= 1

        return dp[0]
    
if '__main__' == __name__:
    sol =Solution()
    print(sol.wordBreak(s="neetcode", wordDict=["neet","code"]))