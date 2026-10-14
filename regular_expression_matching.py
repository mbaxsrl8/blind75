# Tags: 2-d-dynamic-programming, string, needs-review
# You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

# Return true if the pattern matches the entire input string, otherwise return false.

# '.' Matches any single character
# '*' Matches zero or more of the preceding element.

from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []
        for c in p:
            if c == '*':
                pattern[-1] = pattern[-1] + '*'
            else:
                pattern.append(c)
        
        @cache       
        def compare(i: int, j: int) -> bool:
            if i == len(s):
                if j == len(pattern):
                    return True
                else:
                    if pattern[j][-1] != '*':
                        return False
                    return compare(i, j + 1)
            if j == len(pattern):
                return False
            
            if pattern[j][-1] == '*':
                if s[i] == pattern[j][0]:
                    c = s[i]
                    while i < len(s) and s[i] == c:
                        if compare(i, j + 1):
                            return True
                        i += 1
                    return compare(i, j + 1)
                elif pattern[j][0] == '.':
                    while i < len(s):
                        if compare(i, j + 1):
                            return True
                        i += 1
                    return compare(i, j + 1)
                else:
                    return compare(i, j + 1)
                            
            else:
                if s[i] == pattern[j] or pattern[j] == '.':
                    return compare(i + 1, j + 1)
                else:
                    return False
            
        return compare(0, 0)
                
        
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.isMatch(s = "aa", p=".*..a*"))
    # print(sol.isMatch(s = "aaa", p = "ab*a"))
    # print(sol.isMatch(s = "bbbbba", p = ".*a*a"))
    # print(sol.isMatch(s = "a", p = "ab*"))
    # print(sol.isMatch(s = "aaa", p="ab*ac*a"))
    # print(sol.isMatch(s = "mississippi", p="mis*is*p*."))
    # print(sol.isMatch(s = "aab", p="c*a*b"))
    # print(sol.isMatch(s = "aa", p = ".b"))
    print(sol.isMatch(s = "nnn", p = "n*"))
    # print(sol.isMatch(s = "xyz", p = ".*z"))
    # print(sol.isMatch(s = "aa", p = "a"))