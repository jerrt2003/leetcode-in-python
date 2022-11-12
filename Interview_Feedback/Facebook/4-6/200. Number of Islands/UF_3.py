# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        uf = UnionFind(grid)
        res = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    r = uf.find(n * i + j)
                    if r not in res:
                        res.add(r)
                        stack = [(i, j)]
                        while stack:
                            ii, jj = stack.pop(0)
                            for x, y in [(ii - 1, jj), (ii + 1, jj), (ii, jj - 1), (ii, jj + 1)]:
                                if 0 <= x < m and 0 <= y < n and grid[i][j] == '1' and uf.parent[x * n + y] != r and (x,y) not in stack:
                                    uf.union(ii * n + jj, x * n + y)
                                    stack.append((x, y))
        return len(res)


class UnionFind(object):
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.parent = [-1 for _ in range(len(matrix) * len(matrix[0]))]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    self.parent[n * i + j] = n * i + j

    def find(self, pt):
        if self.parent[pt] != pt:
            self.parent[pt] = self.find(self.parent[pt])
        return self.parent[pt]

    def union(self, pt1, pt2):
        r1 = self.find(pt1)
        r2 = self.find(pt2)
        if r1 != r2:
            self.parent[r2] = r1



assert Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1