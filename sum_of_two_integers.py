# Tags: bit-manipulation

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(-1, 1))
