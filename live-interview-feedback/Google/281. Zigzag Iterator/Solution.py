# -*- coding: utf-8 -*-
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        T: O(n)
        :type v1: List[int]
        :type v2: List[int]
        """
        i, j = 0, 0
        self.lst = []
        while i < len(v1) and j < len(v2):
            self.lst.append(v1[i])
            self.lst.append(v2[j])
            i += 1
            j += 1
        if i < len(v1):
            self.lst += v1[i:]
        if j < len(v2):
            self.lst += v2[j:]

    def next(self):
        """
        T:O(1)
        :rtype: int
        """
        return self.lst.pop(0)

    def hasNext(self):
        """
        T:O(1)
        :rtype: bool
        """
        return len(self.lst) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())