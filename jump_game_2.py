# Tags: greedy, breadth-first-search, needs-review
class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest
                if farthest == len(nums) - 1:
                    return jumps

        return jumps
        
                    
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.jump(nums=[2,4,1,1,1,1]))
