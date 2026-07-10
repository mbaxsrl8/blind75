from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while r > l:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] >= heights[r]:
                r = r - 1
            else:
                l = l + 1
        
        return res
        

if '__main__' == __name__:
    sol = Solution()
    print(sol.maxArea([2,2,2]))