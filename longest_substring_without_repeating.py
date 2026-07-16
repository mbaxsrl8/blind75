# Tags: hash-map, sliding-window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        cache = set()
        res = 0
        while r < len(s):
            if s[r] not in cache:
                cache.add(s[r])
                r += 1
            else:
                res = max(res, r-l)
                while l <= r and s[l] != s[r]:
                    cache.remove(s[l])
                    l += 1
                l += 1
                r += 1
        res = max(res, r-l)
        return res
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "pwwkew"))