# Tags: array, bit-manipulation

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            res ^= i ^ nums[i]
            
        return res ^ len(nums)
        
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.missingNumber([1,2,3]))