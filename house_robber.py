# Tags: dp

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1= 0,0
        for money in nums:
            prev2, prev1 = prev1, max(prev2 + money, prev1)
        return prev1
        
        
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.rob(nums = [1,1,3,3]))
