# Tags: backtracking, recursion, sorting
from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                res.append([nums[i]])
            else:
                subRes = self.combinationSum(nums[i:], target - nums[i])
                if len(subRes) > 0:
                    subRes = [list + [nums[i]] for list in subRes]
                    res += subRes
        return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.combinationSum([8,7,4,3], 11))
