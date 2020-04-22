# -*- coding: utf-8 -*-
class Solution(object):
    def findOrientation(self,p1,p2,p3):
        """
        Using slope to find p1, p2 and p3's orientation
        https://www.geeksforgeeks.org/orientation-3-ordered-points/
        :param p1: (x1, y1)
        :param p2: (x2, y2)
        :param p3: (x3, y3)
        :return: clockwise, counterclockwise, colinear
        """
        #s1 = (p2[1]-p1[1])/(p2[0]-p1[0])
        #s2 = (p3[1]-p2[1])/(p3[0]-p1[0])
        v = (p2[1]-p1[1])*(p3[0]-p2[0]) - (p3[1]-p2[1])*(p2[0]-p1[0])
        if v == 0:
            return "colinear"
        elif v > 0:
            return "clockwise"
        else:
            return "couterclockwise"


assert Solution().findOrientation((0,0),(4,4),(1,2)) == "couterclockwise"