# Tags: two-pointers

# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the total amount of water that can be trapped between the bars.
class Solution:
    def trap(self, height: list[int]) -> int:
        l,r=0,len(height)-1
        water = 0
        left_max, right_max = 0, 0
        while l <= r:
            if left_max <= right_max:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
            
        
        return water
    # def trap(self, height: list[int]) -> int:
    #     res = 0
    #     level = 1
    #     highest = max(height)
    #     while level <= highest:
    #         i = 0
    #         while i < len(height):
    #             while i < len(height) and height[i] < level:
    #                 i += 1
    #             while i < len(height) and height[i] >= level:
    #                 i += 1
    #             j = i
    #             while j < len(height) and height[j] < level:
    #                 j += 1
    #             if j != len(height):
    #                 res += j - i
    #             i = j
    #         level += 1
    #     return res
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.trap(height=[0,2,0,3,1,0,1,3,2,1]))
