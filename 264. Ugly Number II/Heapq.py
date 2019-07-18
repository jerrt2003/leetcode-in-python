# -*- coding: utf-8 -*-
import pq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        Solution: heapq (priority queue)
        Time Complexity: O(3*n)
        Space Complexity: O(3*n)
        Perf: Runtime: 896 ms, faster than 8.14% / Memory Usage: 10.9 MB, less than 35.21%
        Inspired By: MySELF!!
        :type n: int
        :rtype: int
        """
        cand = [1]
        for i in range(n-1):
            k = pq.heappop(cand)
            if k*2 not in cand:
                pq.heappush(cand, k * 2)
            if k*3 not in cand:
                pq.heappush(cand, k * 3)
            if k*5 not in cand:
                pq.heappush(cand, k * 5)
        return pq.heappop(cand)

n = 10
print Solution().nthUglyNumber(10)
