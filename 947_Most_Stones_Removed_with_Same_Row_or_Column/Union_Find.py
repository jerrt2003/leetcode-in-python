# -*- coding: utf-8 -*-
class Solution(object):
    def removeStones(self, points):
        UF = {}

        def find(x):
            """
            To find x's ROOT !!!
            :param x:
            :return:
            """
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            """
            To union x, y (e.g. make x's root to become y's root)
            Basically we use y as "base point" to "group" x
            :param x:
            :param y:
            :return:
            """
            UF[x] = UF.setdefault(x, x) # set UF[x] = x if UF[x] is not set yet. If its already set it means it already belongs to a SET
            UF[y] = UF.setdefault(y, y)
            UF[find(x)] = find(y) # To set point x's ROOT to be y's ROOT

        for x, y in points:
            union(x, ~y) # reverse y to avoid x=1 and y=1 situation.

        return len(points) - len({find(x) for x in UF}) # in here we check in total how many dis-joinset we have


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[9,9]]
print Solution().removeStones(stones)

