# -*- coding: utf-8 -*-
class Calender(object):
    def __init__(self, intervals):
        intervals.sort(key=lambda k:k[0])
        mergeInterval = []
        for s, e in intervals:
            if not mergeInterval:
                mergeInterval.append([s, e])
            elif s > mergeInterval[-1][1]:
                mergeInterval.append([s, e])
            elif s <= mergeInterval[-1][1] and e > mergeInterval[-1][1]:
                mergeInterval[-1][1] = e
        self.res = []
        prev_end = 0
        for s, e in mergeInterval:
            self.res += [i for i in range(prev_end, s)]
            prev_end = e

    def query(self, start, end):
        l, r = 0, len(self.res)
        while l < r:
            mid = (l+r-1)/2
            if self.res[mid] >= start:
                r = mid
            else:
                l = mid+1
        start = l
        l, r = 0, len(self.res)
        while l < r:
            mid = (l+r-1)/2
            if self.res[mid] > end:
                r = mid
            else:
                l = mid+1
        end = l-1
        return end - start + 1

calender = Calender([[1,2],[4,6],[5,9],[11,12]])
assert calender.query(3, 7) == 1
assert calender.query(3, 12) == 3