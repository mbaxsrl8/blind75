# Tags: dynamic-programming
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        i = len(nums) - 2 
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])     
        return max(dp)
            
        
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     # recursion
    #     res = 0
    #     dp = [-1] * len(nums)
    #     for i in range(0, len(nums)):
    #         if dp[i] == -1:
    #             dp[i] = self.start_of_i(nums, i, dp)
    #         res = max(res, dp[i])
    #     return res
        
    # def start_of_i(self, nums, i, dp) -> int:
    #     res = 1
    #     if i == len(nums) - 1:
    #         dp[i] = 1
    #         return 1
    #     for j in range(i + 1, len(nums)):
    #         if nums[j] > nums[i]:
    #             if dp[j] == -1:
    #                 dp[j] = self.start_of_i(nums, j, dp)
    #             res = max(res, 1 + dp[j])
    #     return res
        

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     # brute force
    #     return self.recursive(nums, 0, -1001)

    # def recursive(self, nums: List[int], i: int, m: int) -> int:
    #     if i == len(nums) - 1:
    #         if nums[i] > m:
    #             return 1
    #         else:
    #             return 0
    #     # choose to add this number
    #     # find next value that's greater than val
    #     res1 = 1
    #     if nums[i] <= m:
    #         res1 = 0
    #     else:
    #         res1 += self.recursive(nums, i + 1, nums[i])
    #     # choose to skip this number
    #     res2 = self.recursive(nums, i + 1, m)
    #     return max(res1, res2)


if "__main__" == __name__:
    sol = Solution()
    print(sol.lengthOfLIS([0,1,0,3,2,3]))
