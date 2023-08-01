import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.ans = []
        self.node_neighbor = collections.defaultdict(list)
        for s, e in tickets:
            heapq.heappush(self.node_neighbor[s], e)
        self.dfs("JFK")

        return self.ans[::-1]

    def dfs(self, stop):
        while self.node_neighbor[stop]:
            next_stop = heapq.heappop(self.node_neighbor[stop])
            self.dfs(next_stop)
        self.ans.append(stop)
