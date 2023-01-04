from typing import List

class MinStack:

    def __init__(self):
        # maintain a stack element store 2 number
        # [curr, curr_min]
        self.min_stack: List[List[int, int]] = []
        
    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append([val, val])
        else:
            self.min_stack.append([val, min(self.getMin(), val)])

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]
        
    def getMin(self) -> int:
        return self.min_stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()