# Tags: hash-map, string, sorting
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict()
        for word in strs:
            key = str(sorted(word))
            if key not in cache:
                cache[key] = [word]
            else:
                cache.get(key).append(word)
        return list(cache.values())
        
        
if '__main__' == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))