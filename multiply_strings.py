# Tags: math
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2num = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        def convertNum(word: str) -> int:
            result = 0
            for i in range(len(word) - 1, -1, -1):
                result += str2num[word[i]] * (10 ** (len(word) - 1 - i))
            return result
        
        product = convertNum(num1) * convertNum(num2)
        if product == 0: return "0"
        
        num2str = {v:k for k, v in str2num.items()}
        result = ''  
        while product:
            result = num2str[product % 10] + result
            product = product // 10
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply(num1 = "0", num2 = "0"))
