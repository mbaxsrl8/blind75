# Tags: dynamic-programming

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        j = i
        res = nums[0]
        while i < len(nums):
            prefix = 0
            while j < len(nums):
                if prefix < 0:
                    i = j
                    break
                res = max(res, prefix + nums[j])
                prefix = prefix + nums[j]
                j = j + 1
                if j == len(nums):
                    i = j
        return res
            
            
if "__main__" == __name__:
    sol = Solution()
    print(sol.maxSubArray([-1]))