import collections


class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        T:O(V+E) S:O(V+E)
        Runtime: 1276 ms, faster than 5.26% of Python online submissions for All Paths from Source Lead to Destination.
        Memory Usage: 17.7 MB, less than 69.33% of Python online submissions for All Paths from Source Lead to Destination.
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for s, e in edges:
            graph[s].append(e)

        visit = [0 for _ in range(n)]

        def dfs(i):
            if i not in graph.keys():
                return i == destination
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for nxt_i in graph[i]:
                if not dfs(nxt_i):
                    return False
            visit[i] = 1
            return True

        return dfs(source)



print Solution().leadsToDestination(3, [[0,1],[0,2]], 0, 2)
print Solution().leadsToDestination(4, [[0,1],[0,3],[1,2],[2,1]], 0, 3)
print Solution().leadsToDestination(4, [[0,1],[0,2],[1,3],[2,3]], 0, 3)
print Solution().leadsToDestination(3, [[0,1],[1,1],[1,2]], 0, 2)
print Solution().leadsToDestination(1, [[0,0]], 0, 0)