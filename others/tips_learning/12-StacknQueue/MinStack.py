from math import inf


class MinStack:

    def __init__(self):
        self.value_stack = []
        self.min_stack = []
        self.min = inf

    def push(self, val: int) -> None:
        self.value_stack.append(val)
        self.min = min(self.min, val)
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.value_stack.pop()
        self.min_stack.pop()
        self.min = self.min_stack[-1] if self.min_stack else inf

    def top(self) -> int:
        return self.value_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()