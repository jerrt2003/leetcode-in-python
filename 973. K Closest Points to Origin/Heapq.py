# -*- coding: utf-8 -*-
import pq, math
class Solution(object):
    def kClosest(self, points, K):
        """
        Solution: Heapq
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 736 ms, faster than 28.82% / Memory Usage: 18.2 MB, less than 5.01%
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        neareast = []
        for i, j in points:
            pq.heappush(neareast, (-math.sqrt(i * i + j * j), [i, j]))
            if len(neareast) > K:
                pq.heappop(neareast)
        res = []
        while neareast:
            res.append(pq.heappop(neareast)[1])
        return res


points = [[3, 3], [5, -1], [-2, 4]]
K = 2

print Solution().kClosest(points, K)