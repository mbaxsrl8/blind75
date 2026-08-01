# Tags: dp

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dest = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < dest - i:
                continue
            dest = i
        return dest == 0
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump(nums = [1,2,1,0,1]))
