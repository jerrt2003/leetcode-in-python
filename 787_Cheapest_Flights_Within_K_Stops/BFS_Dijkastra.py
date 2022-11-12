# -*- coding: utf-8 -*-
import pq, collections
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        Solution: BFS + Dijsktra
        Time Complexity:
        Space Complexity: O(n) (n: heap length)
        Inspired By:
        - https://leetcode.com/problems/cheapest-flights-within-k-stops/solution/
        - https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
        TP:
        - Using Dijkstra Algorithm but at same time keep the stops under K
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        best = dict()
        pq = [(0, 0, src)]
        while pq:
            curr_cost, curr_stop, curr_city = pq.heappop(pq)
            if curr_stop > K+1 or curr_cost > best.get((curr_stop, curr_city), float('inf')):
                continue
            if curr_city == dst:
                return curr_cost
            for next_stop, cost in graph[curr_city].iteritems():
                new_cost = cost + curr_cost
                if new_cost < best.get((curr_stop+1, dst), float('inf')):
                    best[(curr_stop+1, next_stop)] = new_cost
                    pq.heappush(pq, (new_cost, curr_stop + 1, next_stop))
        return -1

'''
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
'''

'''
n = 5
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1
'''

n = 5
flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
src = 0
dst = 4
k = 1


print Solution().findCheapestPrice(n, flights, src, dst, k)