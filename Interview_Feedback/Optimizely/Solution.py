# -*- coding: utf-8 -*-
class Solution(object):
    def findLakeElavation(self, arr):
        """
        :param arr:
        :return:
        """
        pt1, pt2 = None, None
        res = []
        for a in arr:
            if pt1 is None:
                pt1 = a
                continue
            elif pt2 is None:
                pt2 = a
                continue
            else:
                if a <= pt2:
                    continue
                elif pt2 < a <= pt1:
                    pt2 = a
                else:
                    res.append(abs(pt2 - pt1))
                    pt1 = a
                    pt2 = None
        return res

assert Solution().findLakeElavation([8, 11, 6, 9, 5]) == [8, 9, 5]