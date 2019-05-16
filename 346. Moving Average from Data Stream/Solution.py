# -*- coding: utf-8 -*-
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = []
        self.size = size
        self.sum = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.window.append(val)
            self.sum += val
            return float(self.sum) / len(self.window)
        else:
            firstValue = self.window.pop(0)
            diff = val - firstValue
            self.sum += diff
            self.window.append(val)
            return float(self.sum) / len(self.window)

obj = MovingAverage(3)
print obj.next(3)
print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)