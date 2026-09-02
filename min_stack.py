# Tags: stack, monotonic-queue, design
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minQueue = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minQueue) == 0 or val <= self.minQueue[-1]:
            self.minQueue.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minQueue[-1] == val:
            self.minQueue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minQueue[-1]

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(-2)
    minStack.push(-3)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
