# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(grid)
        island = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    r = uf.find(i * n + j)
                    if r not in island:
                        island.add(r)
                        stack = [(i, j)]
                        while stack:
                            x, y = stack.pop(0)
                            for ii, jj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1' and uf.parent[ii * n + jj] != r and (ii, jj) not in stack:
                                    uf.union(x * n + y, ii * n + jj)
                                    stack.append((ii, jj))
        return len(island)


class UnionFind(object):
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.parent = [-1 for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    self.parent[i * n + j] = i * n + j

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        r1 = self.find(node1)
        r2 = self.find(node2)
        if r1 != r2:
            self.parent[r2] = r1

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print Solution().numIslands(grid)

