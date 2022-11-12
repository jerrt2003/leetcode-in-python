import collections
from bisect import insort


class Solution(object):
    def findItinerary(self, tickets):
        """
        Facebook
        Topo Sort
        DFS
        T:O(V+E) S:O(E)
        Runtime: 68 ms, faster than 60.33% of Python online submissions for Reconstruct Itinerary.
        Memory Usage: 13.2 MB, less than 62.07% of Python online submissions for Reconstruct Itinerary.
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        fly_map = collections.defaultdict(list)
        for src, dst in tickets:
            insort(fly_map[src], dst)

        ans = []

        def dfs(curr):
            while fly_map[curr]:
                nxt = fly_map[curr][0]
                fly_map[curr].remove(nxt)
                dfs(nxt)
            ans.append(curr)

        dfs('JFK')
        return ans[::-1]

print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])