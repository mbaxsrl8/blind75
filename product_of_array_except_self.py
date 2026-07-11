# Tags: prefix-suffix

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # first loop to compute prefix
        result[0] = 1
        i = 1
        while i < len(nums):
            result[i] = result[i - 1] * nums[i - 1]
            i = i + 1
        # second loop to compute postfix hence the final result
        j = -1
        postfix = 1
        while -j <= len(nums):
            result[j] = result[j] * postfix
            postfix = postfix * nums[j]
            j = j -1
        return result
            
            

if "__main__" == __name__:
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 4, 6]))
