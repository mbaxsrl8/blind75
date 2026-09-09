# Tags: linked-list, two-pointers
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
if __name__ == "__main__":
    sol = Solution()
    # print(sol.findDuplicate([1,2,3,2,2]))
    # print(sol.findDuplicate(nums=[18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]))
    print(sol.findDuplicate(nums=[3,1,3,4,2]))
