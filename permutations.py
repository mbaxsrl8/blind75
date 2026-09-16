# Tags: backtracking
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        selected = set()
        
        def backtrack():
            if len(path) ==len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in selected:
                    continue
                path.append(num)
                selected.add(num)
                backtrack()
                path.pop()
                selected.remove(num)
                
        backtrack()
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute(nums = [1,2,3]))
