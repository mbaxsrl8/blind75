# Tags: review-priority, binary-search, rotated-array

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[l] < nums[m + 1]:
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
