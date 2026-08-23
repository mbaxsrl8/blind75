# Tags: review-priority, binary-search, rotated-array

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m -1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        if nums[r] == target:
            return r
        else: return -1
               
    
        
        
if "__main__" == __name__:
    sol = Solution()
    print(sol.search([5,1,2,3,4], 1))
