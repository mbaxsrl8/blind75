from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[l]:
            return nums[l]
        m = (r - l) // 2 + l
        while m > l:
            if nums[m] > nums[l]:
                # we're still in left portion
                l = m
            else:
                r = m
            m = (r - l) // 2 + l
            
        return nums[r]
        

if "__main__" == __name__:
    sol = Solution()
    print(sol.findMin([4,5,6,7]))