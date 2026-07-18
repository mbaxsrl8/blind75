# Tags: string, stack
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[', ')':'(', ']':'[', '}':'{'}
        
        stack = deque()
        for c in s:
            if c not in map.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != map[c]:
                    return False
                
        return len(stack) == 0
        

if '__main__' == __name__:
    sol = Solution()
    print(sol.isValid("("))