# Tags: dynamic-programming, 2-d-dynamic-programming
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        level = {0: 1}
        next_level = {}
        for num in nums:
            for subAmount, count in level.items():
                if subAmount + num not in next_level:
                    next_level[subAmount + num] = 0
                next_level[subAmount + num] = next_level[subAmount + num] + count
                if subAmount - num not in next_level:
                    next_level[subAmount - num] = 0
                next_level[subAmount - num] = next_level[subAmount - num] + count
            level = next_level
            next_level = {}
        return level.get(target, 0)
            
    
    # def findTargetSumWays(self, nums: list[int], target: int) -> int:
    #     def backtrack(index: int, amount: int) -> int:
    #         if index == len(nums):
    #             return 1 if amount == 0 else 0
    #         result = 0
    #         result += backtrack(index + 1, amount - nums[index])
    #         result += backtrack(index + 1, amount + nums[index])
    #         return result
    #     return backtrack(0, target)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findTargetSumWays(nums = [2,2,2], target = 2))
