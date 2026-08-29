# Tags: dynamic-programming

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        prev = 1
        prev_neg = None
        for num in nums:
            if num >= 0:
                if prev_neg != None:
                    prev_neg = prev_neg * num
                if prev >0:
                    cur = num * prev
                else:
                    cur = num
            else:
                if prev_neg != None:
                    cur = prev_neg * num
                else:
                    cur = num
                prev_neg = num if prev <=0 else prev*num
            res = max(res, cur)
            prev = cur
        
        return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.maxProduct([2,-5,-2,-4,3]))
