# Tags: two-pointers, sliding-window, hash-map

# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        window = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        l,r = 0,0
        validCount = 0
        while validCount < len(s1):
            while r < len(s2) and s2[r] not in need:
                r += 1
            if r == len(s2):
                return False
            l = r-validCount
            while r < len(s2) and s2[r] in need:
                if window.get(s2[r], 0) == need[s2[r]]:
                    break              
                validCount += 1
                window[s2[r]] = window.get(s2[r], 0) + 1
                r += 1
            if validCount == len(s1):
                return True
            elif r == len(s2):
                return False
            while s2[l] != s2[r]:
                window[s2[l]] = window[s2[l]] - 1
                validCount -= 1
                l += 1
            l += 1
            r += 1
                    
        return False
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.checkInclusion(s1="hello",s2="ooolleoooleh"))
