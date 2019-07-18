# -*- coding: utf-8 -*-
import heapq as pq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for num in nums:
            pq.heappush(q, num)
            while len(q) > k:
                pq.heappop(q)
        return pq.heappop(q)