from typing import List

# Two Sum
# Easy
# Topics
# Company Tags
# Hints
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores value -> index for numbers we have already seen.
        helpMap = {}

        # Traverse the list once and try to find a matching pair on the fly.
        for i, num in enumerate(nums):
            # We need this value to complete the target sum.
            complement = target - num

            # If complement was seen earlier, we found the valid pair.
            if complement in helpMap:
                return [helpMap[complement], i]
            else:
                # Save current number and index for future complement checks.
                helpMap[num] = i