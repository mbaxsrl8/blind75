# Tags: backtracking, review-priority
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            result.extend([subset + [num] for subset in result])
        return result
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets(nums = [1,2,3]))
