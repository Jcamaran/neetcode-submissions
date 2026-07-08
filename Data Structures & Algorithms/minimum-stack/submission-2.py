class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_s = self.getMin()
        if min_s == None or min_s > val:
            min_s = val
        self.stack.append([val,min_s])
        

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

        

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
        
