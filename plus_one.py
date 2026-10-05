# Tags: math
from collections import deque

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        output = deque()
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            res = digits[i] + carry
            if res > 9:
                res = res % 10
                carry = 1
            else:
                carry = 0
            output.appendleft(res)
        if carry:
            output.appendleft(carry)
        return list(output)
            
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne(digits = [9,9,9]))