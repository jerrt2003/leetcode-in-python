import heapq
import collections

class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        Minimum Spanning Tree (MST)
        T:O((E+V)log(V) S:O(V)
        Runtime: 568 ms, faster than 23.81% of Python online submissions for Optimize Water Distribution in a Village.
        Memory Usage: 20.3 MB, less than 100.00% of Python online submissions for Optimize Water Distribution in a Village.
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        self.graph = collections.defaultdict(list) # from: (to, cost)
        for s, d, c in pipes:
            self.graph[s].append((d, c))
            self.graph[d].append((s, c))
        count = 0
        total_cost = 0
        visit = set()
        pq = []
        for i, v in enumerate(wells):
            heapq.heappush(pq, (v, i+1)) #(cost, dest)
        while count < n:
            curr_cost, curr_node = heapq.heappop(pq)
            if curr_node in visit: continue
            total_cost += curr_cost
            count += 1
            visit.add(curr_node)
            for next_node, cost_to_next in self.graph[curr_node]:
                heapq.heappush(pq, (cost_to_next, next_node))
        return total_cost

print Solution().minCostToSupplyWater(3,[1,2,2],[[1,2,1],[2,3,1]])
