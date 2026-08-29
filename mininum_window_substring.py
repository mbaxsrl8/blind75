# Tags: sliding-window, hash-map, string
class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        cache_t = {}
        for c in t:
            cache_t[c] = cache_t.get(c, 0) + 1
        
        cache_cur = {}
        valid_total = 0
        l,r=0,-1
        while r < len(s):
            while r < len(s) and valid_total != len(t):
                r += 1
                while r < len(s) and s[r] not in cache_t.keys():
                    r += 1
                if r >= len(s):
                    return res
                cache_cur[s[r]] = cache_cur.get(s[r], 0) + 1
                if cache_cur[s[r]] <= cache_t[s[r]]:
                    valid_total += 1
                    
            while valid_total == len(t):
                while s[l] not in cache_t.keys():
                    l+=1
                if res == "" or r-l+1 < len(res):
                    res = s[l:r+1]
                cache_cur[s[l]] = cache_cur[s[l]] - 1
                if cache_cur[s[l]] < cache_t[s[l]]:
                    valid_total -= 1
                l += 1
                
                
        return res
        
    
    # def minWindow(self, s: str, t: str) -> str:
    #     res = ""
    #     min_len = len(s)
    #     overall_count = 0
    #     map_need = {}
    #     for c in t:
    #         map_need[c] = map_need.get(c, 0) + 1
    #     map_have = {}

    #     l = 0
    #     r = 0
    #     while r < len(s):
    #         if s[r] not in map_need.keys():
    #             r += 1
    #             continue
    #         map_have[s[r]] = map_have.get(s[r], 0) + 1
    #         if map_have[s[r]] <= map_need[s[r]]:
    #             overall_count += 1
    #         while overall_count == len(t):
    #             if (r - l + 1) <= min_len:
    #                 res = s[l : r + 1]
    #                 min_len = len(res)
    #             if s[l] in map_need.keys():
    #                 map_have[s[l]] = map_have[s[l]] - 1
    #                 if map_have[s[l]] < map_need[s[l]]:
    #                     overall_count -= 1
    #             l += 1
                
                    
    #         r += 1

    #     return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.minWindow(s="xyz", t="xyz"))
