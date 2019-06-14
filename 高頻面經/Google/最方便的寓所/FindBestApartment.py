# -*- coding: utf-8 -*-
class Solution(object):
    def findBestAparatment(self, street, requireList):
        distList = [{req: float('inf') for req in requireList} for _ in range(len(street))]
        for i in range(len(street)):
            street[i] = set(street[i])
            for req in requireList:
                if req in street[i]:
                    distList[i][req] = 0
                elif i-1 >= 0:
                    distList[i][req] = distList[i-1][req]+1
        for j in range(len(street)-1, -1, -1):
            for req in requireList:
                if req in street[j]: continue
                elif j+1 < len(street):
                    distList[j][req] = min(distList[j][req], distList[j+1][req]+1)
        res, minDist = list(), float('inf')
        for i in range(len(distList)):
            d = max(distList[i].values())
            if d < minDist:
                minDist = d
                res = [i]
            elif d == minDist:
                res.append(i)
        return res

street = [["Store", "School", "Museum"],["Hospital", "Restaurant"],["School", "Restaurant"],[],["Museum"]]
requirements = ["Store", "Museum", "Restaurant"]
assert sorted(Solution().findBestAparatment(street, requirements)) == [0, 1]
requirements = ["Hospital", "Restaurant"]
assert sorted(Solution().findBestAparatment(street, requirements)) == [1]