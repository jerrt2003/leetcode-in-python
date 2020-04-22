# -*- coding: utf-8 -*-
import pq
class Solution(object):
    def mergeKSortedLists(self, lists):
        """
        Time: O(nlog(k))
        Space: O(n)
        :param lists:
        :return:
        """
        pq = []
        res = []
        for idx, list in enumerate(lists):
            pq.heappush(pq, (list.pop(0), idx))
        while pq:
            val, idx = pq.heappop(pq)
            res.append(val)
            if lists[idx]:
                pq.heappush(pq, (lists[idx].pop(0), idx))
        return res

lists = [
    [1,2,3,9],
    [2,4],
    [5,7,13],
    [1,6,12]
]

assert Solution().mergeKSortedLists(lists) == [1,1,2,2,3,4,5,6,7,9,12,13]