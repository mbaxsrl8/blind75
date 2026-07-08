from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[r] >= nums[l]:
            return nums[l]
    
        while r > l:
            m = (l + r) // 2
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            if nums[m] > nums[l]:
                # we're still in left portion
                l = m + 1
            else:
                r = m
        return nums[r]
        

if "__main__" == __name__:
    sol = Solution()
    print(sol.findMin([2]))
    print(sol.findMin([2,1]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([3,4,5,6,1,2]))
    print(sol.findMin([3,4,5,1,2]))