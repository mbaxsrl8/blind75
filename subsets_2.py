# Tags: backtracking
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = [[]]
        i = 0
        while i < len(nums):
            previous = [[nums[i]] + subRes for subRes in result]
            result.extend(previous)
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                previous = [[nums[i]] + subRes for subRes in previous]
                result.extend(previous)
                j += 1
            i = j
        
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup(nums = [1,2,1]))
