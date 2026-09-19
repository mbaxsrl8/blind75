# Tags: backtracking
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        number_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        path = []
        
        def backtrack(start: int):
            if start == len(digits):
                result.append("".join(path))
                return

            for c in number_map[digits[start]]:
                path.append(c)
                backtrack(start + 1)
                path.pop()
                
        backtrack(0)
        return result
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(digits = "34"))
        
