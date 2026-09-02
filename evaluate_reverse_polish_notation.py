# Tags: stack
from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = set()
        operations.add('+')
        operations.add('-')
        operations.add('*')
        operations.add('/')
        
        stack = deque()
        i = 0
        while i < len(tokens):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                val = 0
                if tokens[i] == '+':
                    val = num1 + num2
                elif tokens[i] == '-':
                    val = num1 - num2
                elif tokens[i] == '*':
                    val = num1 * num2
                else:
                    val = int(num1 / num2)
                stack.append(val)
            i += 1
        return stack.pop()
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
