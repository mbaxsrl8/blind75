# Tags: math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        result = 1
        if n > 0:
            for i in range(n):
                result *= x
        else:
            for i in range(-n):
                result /= x
                if abs(result) < 0.00001:
                    return 0.00000
                
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(x = 2.00000, n = -3))
