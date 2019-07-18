# -*- coding: utf-8 -*-
class MyCalendarTwo(object):

    def __init__(self):
        self.calender = []
        self.overbook = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overbook:
            if start < j and i < end:
                return False
        for i, j in self.calender:
            if start < j and i < end:
                self.overbook.append((max(i, start), min(j, end)))
            self.calender.append((start, end))
            return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)