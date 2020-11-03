# -*- coding: utf-8 -*-
import random
class Solution:
    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        k = random.randint(1, self.ranges[-1])
        l, r = 0, len(self.ranges)
        while l < r:
            m = (l+r-1)/2
            if self.ranges[m] >= k:
                r = m
            else:
                l = m+1
        x1, y1, x2, y2 = self.rects[l]
        return [random.randint(x1,x2),random.randint(y1,y2)]