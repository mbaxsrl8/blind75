# Tags: hash-map, string, sorting
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same effect as hashmap
        return Counter(s) == Counter(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting doesn't use extra mem so can think of space complexity is O(1)
        return sorted(s) == sorted(t)