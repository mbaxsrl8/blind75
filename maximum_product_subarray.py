# Tags: array, dynamic-programming

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        res = nums[i]
        max_prefix = 1
        min_prefix = 1
        while i < len(nums):
            val = nums[i]
            res = max(res, max_prefix * val, min_prefix * val, val)
            # if it's 0 we need to reset a neutral number for both max and min prefix
            if val == 0:
                max_prefix = 1
                min_prefix = 1
            else:
                next_max_prefix = max(max_prefix * val, min_prefix * val, val)
                next_min_prefix = min(max_prefix * val, min_prefix * val, val)
                max_prefix = next_max_prefix
                min_prefix = next_min_prefix
            i = i + 1
        return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.maxProduct([3, -1, 4]))
