# Tags: bit-manipulation
# You are given a signed 32-bit integer x.

# Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

# Solve the problem without using integers that are outside the signed 32-bit integer range.
class Solution:
    def reverse(self, x: int) -> int:
        ceiling = 2 ** 31 - 1
        negetive = False
        if x < 0:
            negetive = True
            x = -x
        numList = []
        while x:
            numList.append(x % 10)
            x = x // 10
        res = 0
        for i in range(0, len(numList)):
            digit = numList[i]
            if res > ceiling // 10 or (res == ceiling // 10 and digit > ceiling % 10): return 0
            res = res * 10 + digit
        
        return res if not negetive else -res
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(-2147483412))