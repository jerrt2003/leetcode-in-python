import collections


class Solution(object):
    def minReorder(self, n, connections):
        """
        DFS
        T:O(n) S:O(n)
        Runtime: 944 ms, faster than 64.94% of Python online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
        Memory Usage: 43.3 MB, less than 39.35% of Python online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for s, e in connections:
            graph[s].append((e, 1))
            graph[e].append((s, -1))
        visit = set()
        self.count = 0

        def dfs(node):
            for dest, dir in graph[node]:
                if dest in visit:
                    continue
                visit.add(dest)
                if dir == 1:
                    self.count += 1
                dfs(dest)

        visit.add(0)
        dfs(0)
        return self.count


print Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
print Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])