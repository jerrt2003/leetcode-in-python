class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        UnionFind
        T:O(n) S:O(n)
        Runtime: 44 ms, faster than 86.75% of Python online submissions for Redundant Connection II.
        Memory Usage: 13 MB, less than 73.33% of Python online submissions for Redundant Connection II.
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        incoming = [0 for _ in range(N+1)]
        uf = UnionFind(N)
        edge1, edge2, circle = None, None, None
        for i, v in edges:
            if incoming[v] != 0:
                edge1 = (incoming[v], v)
                edge2 = (i, v)
            else:
                incoming[v] = i
                if uf.union(i, v):
                    circle = (i, v)
        if edge1 and edge2:
            if not circle:
                return edge2
            else:
                return edge1
        return circle

class UnionFind(object):
    def __init__(self, N):
        self.parent = range(N+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px
            return False
        return True

print Solution().findRedundantDirectedConnection([[1,2], [1,3], [2,3]])