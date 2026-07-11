# Tags: bit-manipulation

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res
        

if '__main__' == __name__:
    sol = Solution()
    print(sol.reverseBits(0b00000000000000000000000000010101))