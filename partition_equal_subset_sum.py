# Tags: backtracking, dynamic-programming, needs-review
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # backward dp. ensure each element is used only once
        # if not use backward DP, need 2-D DP
        # dp[i][s]: Can we make sum s using only the first i numbers?
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
    # def canPartition(self, nums: list[int]) -> bool:
    #     sumNums = sum(nums)
    #     if sumNums % 2 == 1:
    #         return False
    #     half = sumNums // 2
    #     nums = sorted(nums)
    #     def backTrack(i:int, target: int) -> bool:
    #         if target == 0:
    #             return True
    #         for p in range(i, len(nums)):
    #             if nums[p] > target:
    #                 break
    #             if backTrack(p + 1, target - nums[p]):
    #                 return True
    #         return False
    
    #     return backTrack(0, half)
                
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition(nums = [1,2,3,4]))
