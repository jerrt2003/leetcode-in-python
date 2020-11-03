# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        Time: O(n(log(n))
        Space: O(n)
        Perf: Runtime: 260 ms, faster than 62.71% / Memory Usage: 14.6 MB, less than 69.62%
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        maps = zip(quality, wage)
        maps.sort(key=lambda p: p[1]/float(p[0]))
        totalQ, minWage, pq, ratio = 0, float('inf'),[], 0
        for q, w in maps:
            totalQ += q
            heapq.heappush(pq, -q)
            if len(pq) == K:
                minWage = min(minWage, totalQ*(w/float(q)))
                totalQ += heapq.heappop(pq)
        return minWage

quality = [10,20,5]
wage = [70,50,30]
K = 2

assert Solution().mincostToHireWorkers(quality, wage, K) == 105.0