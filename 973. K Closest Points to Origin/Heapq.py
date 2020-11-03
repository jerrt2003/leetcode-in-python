# -*- coding: utf-8 -*-
import heapq


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
        # neareast = []
        # for i, j in points:
        #     pq.heappush(neareast, (-math.sqrt(i * i + j * j), [i, j]))
        #     if len(neareast) > K:
        #         pq.heappop(neareast)
        # res = []
        # while neareast:
        #     res.append(pq.heappop(neareast)[1])
        # return res
        """
        T:O(nlogn) S:O(n)
        Runtime: 560 ms, faster than 95.50% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 18.4 MB, less than 82.23% of Python online submissions for K Closest Points to Origin.
        """
        # points.sort(key=lambda x: x[0]*x[0]+x[1]*x[1])
        # return points[:K]
        """
        T:O(nlog(k)) S:O(n)
        Runtime: 608 ms, faster than 86.11% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 19.3 MB, less than 26.08% of Python online submissions for K Closest Points to Origin.
        """
        return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])


points = [[3, 3], [5, -1], [-2, 4]]
K = 2

print Solution().kClosest(points, K)