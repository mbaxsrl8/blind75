from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[r] >= nums[l]:
            return nums[l]
        m = (l + r) // 2
        while m > l:
            if nums[m] > nums[l]:
                # we're still in left portion
                l = m
            else:
                r = m
            m = (l + r) // 2
            
        return nums[m + 1]
        

if "__main__" == __name__:
    sol = Solution()
    print(sol.findMin([3,4,5,6,1,2]))
    print(sol.findMin([3,4,5,1,2]))