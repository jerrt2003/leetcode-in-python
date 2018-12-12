# -*- coding: utf-8 -*-
class MinStack(object):

    def __init__(self):
        """
        Solution: Using list to create a stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        TP:
        - To create 2 list, one as stack the other one will be used to keep the min
        initialize your data structure here.
        """
        self.q = []
        self.min_q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        if not self.min_q or x <= self.min_q[-1]:
            self.min_q.append(x)


    def pop(self):
        """
        :rtype: void
        """
        tmp = self.q.pop()
        if self.min_q[-1] == tmp: # if tmp != min_q[-1] then it means the min value must still inside the stack
            self.min_q.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_q[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()