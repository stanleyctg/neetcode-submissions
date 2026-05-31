class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min_temp = self.stack[0]

        for i in range(1,len(self.stack)):
            if min_temp > self.stack[i]:
                min_temp = self.stack[i] 
        return min_temp       
