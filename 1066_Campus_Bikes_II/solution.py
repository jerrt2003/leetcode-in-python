import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        Runtime: 124 ms, faster than 55.76% of Python online submissions for Campus Bikes II.
        Memory Usage: 12.9 MB, less than 79.73% of Python online submissions for Campus Bikes II.
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def manhatten(w, b):
            return abs(workers[w][0]-bikes[b][0])+abs(workers[w][1]-bikes[b][1])

        pq = [(0, 0, 0)] # cost, idx, bikes-taken
        visit = set()
        while pq:
            cost, i, taken = heapq.heappop(pq)
            if i == len(workers):
                return cost
            # if (i, taken) in visit: continue
            if taken in visit: continue
            # visit.add((i, taken))
            visit.add(taken)
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    dis = manhatten(i, j)
                    heapq.heappush(pq, [cost+dis,i+1,taken | (1 << j)])

