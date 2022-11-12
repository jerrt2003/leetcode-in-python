# -*- coding: utf-8 -*-
class pt(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution(object):
    def checkIfSegmentIntersect(self, p1, q1, p2, q2):
        """
        https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
        :param p1:
        :param q1:
        :param p2:
        :param q2:
        :return:
        """

        def findOrientation(p, q, r):
            """
            To return orientation v of points: p, q and r
            if v == 0 --> colinear
            if v == 1 --> clockwise
            if v == -1 --> couter-clockwise
            :param p:
            :param q:
            :param r:
            :return: v
            """
            _res = (q.y-p.y)*(r.x-q.x) - (r.y-q.y)*(q.x-p.x)
            if _res > 0:
                return 1
            elif _res < 0:
                return -1
            else:
                return 0

        def onSegmant(p, q, r):
            """
            to check if q lies between p and r
            :param p:
            :param q:
            :param r:
            :return: boolean
            """
            if min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y):
                return True
            return False

        o1 = findOrientation(p1, q1, p2)
        o2 = findOrientation(p1, q1, q2)
        o3 = findOrientation(p2, q2, p1)
        o4 = findOrientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and onSegmant(p1, p2, q1):
            return True
        if o2 == 0 and onSegmant(p1, q2, q1):
            return True
        if o3 == 0 and onSegmant(p2, p1, q2):
            return True
        if o4 == 0 and onSegmant(p2, q1, q2):
            return True

        return False

p1 = pt(1, 1)
q1 = pt(10, 1)
p2 = pt(1, 2)
q2 = pt(10, 2)

assert Solution().checkIfSegmentIntersect(p1, q1, p2, q2) == False

p1 = pt(10, 1)
q1 = pt(0, 10)
p2 = pt(0, 0)
q2 = pt(10, 10)

assert Solution().checkIfSegmentIntersect(p1, q1, p2, q2) == True