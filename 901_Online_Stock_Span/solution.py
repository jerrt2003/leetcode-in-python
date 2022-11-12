class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        Stack
        T:O(n) S:O(n)
        Runtime: 488 ms, faster than 74.59% of Python online submissions for Online Stock Span.
        Memory Usage: 17.6 MB, less than 90.75% of Python online submissions for Online Stock Span.
        :type price: int
        :rtype: int
        """
        if not self.stack or price < self.stack[-1][0]:
            self.stack.append((price, 1))
        else:
            days = 1
            while self.stack and price >= self.stack[-1][0]:
                _, day = self.stack.pop()
                days += day
            self.stack.append((price, days))
        return self.stack[-1][1]

obj = StockSpanner()
print obj.next(100)
print obj.next(80)
print obj.next(60)
print obj.next(70)
print obj.next(60)
print obj.next(75)
print obj.next(85)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)