# Tags: dp

from typing import List

# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        def rob_line(houses: list[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            prev2, prev1= 0,0
            for money in houses:
                prev2, prev1 = prev1, max(prev2 + money, prev1)
            return prev1
        
        return max(rob_line(nums[1:-2]) + nums[-1], rob_line(nums[:-1]))
    

if '__main__' == __name__:
    sol = Solution()
    print(sol.rob([2,9,8,3,6]))
