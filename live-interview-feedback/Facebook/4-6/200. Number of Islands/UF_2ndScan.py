# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        uf = UnionFind(grid)
        m = len(grid)
        n = len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    root = uf.find(i*n+j)
                    if root not in res: # root is not found --> new island
                        res.add(i*n+j)
                        stack = [(i, j)]
                        while stack:
                            ii, jj = stack.pop(0)
                            for x, y in [(ii+1,jj),(ii-1,jj),(ii,jj+1),(ii,jj-1)]:
                                if 0<=x<m and 0<=y<n and grid[x][y]=='1' and uf.parent[x*n+y] != root:
                                    uf.union(i*n+j, x*n+y)
                                    stack.append((x,y))
        return len(res)

class UnionFind(object):
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.parent = [-1 for _ in range(m*n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[n*i+j] = n*i+j

    def find(self, pt):
        if self.parent[pt] != pt:
            self.parent[pt] = self.find(self.parent[pt])
        return self.parent[pt]

    def union(self, p1, p2):
        r1 = self.find(p1)
        r2 = self.find(p2)
        if r1 != r2:
            self.parent[r2] = r1

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print Solution().numIslands(grid)