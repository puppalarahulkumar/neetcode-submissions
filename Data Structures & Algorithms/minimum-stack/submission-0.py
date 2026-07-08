from collections import deque

class MinStack:

    def __init__(self):
        self.collections=deque()

    def push(self, val: int) -> None:
        self.collections.append(val)

    def pop(self) -> None:
        self.collections.pop()

    def top(self) -> int:
        return self.collections[-1]

    def getMin(self) -> int:
        return min(self.collections)
