# Tags: greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        wildcardsFromLeft = 0
        
        for c in s:
            if c == '(':
                left += 1
            elif c == '*':
                wildcardsFromLeft += 1
            else:
                if left > 0: left -= 1
                elif wildcardsFromLeft > 0: wildcardsFromLeft -= 1
                else: return False
        
        right = 0
        wildcardsFromRight = 0           
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ')':
                right += 1
            elif c == '*':
                wildcardsFromRight += 1
            else:
                if right > 0: right -= 1
                elif wildcardsFromRight > 0: wildcardsFromRight -= 1
                else: return False
            
                
        return left <= wildcardsFromLeft and right <= wildcardsFromRight
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidString(s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
