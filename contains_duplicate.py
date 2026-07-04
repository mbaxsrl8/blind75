from typing import List


class Solution:
    # can also use soring. so only need to compare with the neighbor
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
                
        return False