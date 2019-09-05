# -*- coding: utf-8 -*-
class Solution(object):
    def canVisit(self, itinerary):
        """
        T:O(mn)
        S:O(mn)
        :param itinerary:
        :return:
        """
        m = len(itinerary)
        n = len(itinerary[0])

        DP = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and itinerary[0][j] == 'S':
                    DP[0][j] = True
                else:
                    if itinerary[i][j] == 'S' and (DP[i-1][j-1] or DP[i][j-1]):
                        DP[i][j] = True

        for j in range(n):
            if DP[m-1][n]:
                return True
        return False