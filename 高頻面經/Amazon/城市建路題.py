# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    """
    Union_Find + heapq
    """
    def findMinCost(self, numTotalAvailableCities, numTotalAvailableRoads, roadsAvailable, numNewRoadsConstruct, costNewRoadsConstruct):
        UF = UnionFind(numTotalAvailableCities, roadsAvailable)
        candidate_road = []
        for city1, city2, cost in costNewRoadsConstruct:
            heapq.heappush(candidate_road, (cost, city1, city2))
        res = 0
        while numTotalAvailableRoads < numTotalAvailableCities-1:
            cost, city1, city2 = heapq.heappop(candidate_road)
            r1 = UF.find(city1)
            r2 = UF.find(city2)
            if r1 != r2:
                UF.union(city1, city2)
                numTotalAvailableRoads += 1
                res += cost
        return res

class UnionFind(object):
    """
    Union Find Class
    """
    def __init__(self, numTotalAvailableCities, dots):
        self.UF = {}
        for i in range(1, numTotalAvailableCities+1):
            self.UF[i] = i
        for a, b in dots:
            self.union(a, b)

    def union(self, p1, p2):
        r1 = self.find(p1)
        r2 = self.find(p2)
        if r1 != r2:
            self.UF[r1] = r2

    def find(self, root):
        while root != self.UF[root]:
            root = self.find(self.UF[root])
        return root

numTotalAvailableCities = 6
numTotalAvailableRoads = 3
roadsAvailable = [[1, 4], [4, 5], [2, 3]]
numNewRoadsConstruct = 4
costNewRoadsConstruct = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]

print Solution().findMinCost(numTotalAvailableCities, numTotalAvailableRoads, roadsAvailable, numNewRoadsConstruct, costNewRoadsConstruct)