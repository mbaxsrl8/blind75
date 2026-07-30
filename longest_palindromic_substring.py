# Tags: string, two-pointers

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        if len(s) == 1:
            return res
        i=0
        while i < len(s) - 1:
            j = i + 1
            if s[j] == s[i]:
                while j + 1 < len(s) and s[j + 1] == s[i]:
                    j += 1
                k = j            
                while i-1 >= 0 and j+1 < len(s) and s[i-1] == s[j+1]:
                    i -= 1
                    j += 1
                if j - i + 1 > len(res):
                    res = s[i:j+1]
                i = k
            elif i+2 < len(s) and s[i+2] == s[i]:
                j = i + 2
                k = i
                while k - 1 >= 0 and j < len(s) - 1 and s[k-1] == s[j+1]:
                    k -= 1
                    j += 1
                if j - k + 1 >= len(res):
                    res = s[k:j+1]
                i += 1
            else:
                i += 1
                
                    
        return res
        
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("Abbabdhga"))
