from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while r >= l:
            val = nums[m]
            if val == target:
               return m
           
            # which side has the pivot point?
            if val >= nums[l]:
               # right side has pivot point
                if target >= val or target < nums[l]:
                    l = m + 1
                else:
                    r = m
            else:
                # left side has the pivot point
                if target < val or target > nums[r]:
                    r = m
                else:
                    l = m + 1
            m = (r - l) // 2 + l
            
            
        return -1
               
    
        
        
if "__main__" == __name__:
    sol = Solution()
    print(sol.search([1,2,3,4,5], 5))