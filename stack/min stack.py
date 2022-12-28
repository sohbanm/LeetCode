class MinStack:    
    def __init__(self):
        self.stack = [] #[0] will be the actual value, [1] will be the current minimum value    

    def push(self, val: int) -> None:
        currMin = min(self.getMin(), val)
        self.stack.append([val, currMin])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return float("inf")
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()