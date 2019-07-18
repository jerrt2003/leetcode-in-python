# -*- coding: utf-8 -*-
import pq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        Solution: Heap
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 424 ms, faster than 31.63%  / Memory Usage: 14.1 MB, less than 12.00%
        Inspired By:
        - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/237268/Python-heap-solution-with-clean-code-and-explanation
        - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/
        TP:
        - Using wage[i]/quality[i] as sorting points
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        m = len(quality)
        wkr_ratio = []
        for i in range(m):
            wkr_ratio.append((float(wage[i])/quality[i], quality[i]))
        wkr_ratio.sort()
        h = []
        min_cost = float('inf')
        total_qua = 0
        for ratio, qua in wkr_ratio:
            total_qua += qua
            pq.heappush(h, -qua)
            if len(h) == K:
                min_cost = min(min_cost, total_qua*ratio)
            elif len(h) > K:
                total_qua += pq.heappop(h)
                min_cost = min(min_cost, total_qua*ratio)
        return min_cost