# -*- coding: utf-8 -*-
import heapq
import collections


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        Solution: Heap + Stack
        Perf: Runtime: 676 ms, faster than 87.57% / Memory Usage: 134.8 MB, less than 100.00%
        Time: O(m*n + mlog(n) + mlog(n))
        Space: O(m*n)
        m: len of workers, n: len of bikes
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        w2b = collections.defaultdict(list)
        for i, (wX, wY) in enumerate(workers):
            for j, (bX, bY) in enumerate(bikes):
                dist = abs(wX - bX) + abs(wY - bY)
                w2b[i].append((j, dist))

        for lst in w2b.values():
            lst.sort(key=lambda k: k[1])

        pq = []
        for i in range(len(w2b)):
            j, dist = w2b[i].pop(0)
            heapq.heappush(pq, (dist, i, j))

        visitWorkers = set()
        visitBikes = set()
        res = [0] * len(workers)
        while len(visitWorkers) != len(workers):
            _, w, b = heapq.heappop(pq)
            if w not in visitWorkers and b not in visitBikes:
                res[w] = b
                visitWorkers.add(w)
                visitBikes.add(b)
            else:
                j, dist = w2b[w].pop(0)
                heapq.heappush(pq, (dist, w, j))
        return res


workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
assert Solution().assignBikes(workers, bikes) == [1, 0]