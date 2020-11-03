class MovingAverage(object):

    def __init__(self, size):
        """
        Facebook
        T:O(n) S:O(size)
        Runtime: 64 ms, faster than 63.93% of Python online submissions for Moving Average from Data Stream.
        Memory Usage: 16.2 MB, less than 20.00% of Python online submissions for Moving Average from Data Stream.
        Initialize your data structure here.
        :type size: int
        """
        self.num = []
        self.sum = 0
        self.cap = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.num) == self.cap:
            self.sum -= self.num.pop(0)
        self.sum += val
        self.num.append(val)
        return float(self.sum) / len(self.num)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)