# Tags: array, two-pointers, sorting

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            target = 0 - sorted_nums[i]
            # make sorted_nums[l] + sorted_nums[r] == target
            while r > l:
                two_sum = sorted_nums[l] + sorted_nums[r]
                if two_sum == target:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    x = l + 1
                    while x < r and sorted_nums[x] == sorted_nums[l]:
                        x = x + 1
                    l = x
                elif two_sum > target:
                    r = r - 1
                else:
                    l = l + 1
            
            x = i + 1
            while x < len(nums) - 2 and sorted_nums[x] == sorted_nums[i]:
                x = x + 1
            i = x
            
        return res
        
if "__main__" == __name__:
    sol = Solution()
    print(sol.threeSum([0,0,0,0]))