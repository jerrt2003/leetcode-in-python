# -*- coding: utf-8 -*-
class UnionFind(object):
    def __init__(self, grid_size):
        self.group = grid_size # self.group means the total island number. Although not what question is asking but we can use same code to find total number of island
        self.parent = [i for i in range(grid_size)] # 將2D array扁平化成1D的關係圖
        self.size = [1 for _ in range(grid_size)] # for calculate island size
        self.rank = [0 for _ in range(grid_size)] # for compression


    def find(self, idx):
        while idx != self.parent[idx]:
            self.parent[idx] = self.parent[self.parent[idx]] # path compression
            idx = self.parent[idx]
        return idx

    def union(self, p1, p2):
        if p1 == p2: return
        parent_p1, parent_p2 = self.find(p1), self.find(p2)
        if parent_p1 == parent_p2: return # p1, p2 already in same group
        # p1, p2 not in same group, start union
        self.group -= 1
        if self.rank[parent_p1] > self.rank[parent_p2]:
            self.parent[parent_p2] = parent_p1
            self.size[parent_p1] += self.size[parent_p2]
        elif self.rank[parent_p2] > self.rank[parent_p1]:
            self.parent[parent_p1] = parent_p2
            self.size[parent_p2] += self.size[parent_p1]
        else:
            self.parent[parent_p2] = parent_p1
            self.size[parent_p1] += self.size[parent_p2]
            self.rank[parent_p1] += 1

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        Solution: Union Find
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: https://leetcode.com/problems/max-area-of-island/discuss/180281/python3-union-find-solution
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n)
        idx = -1
        maxarea = 0
        for i in range(m):
            for j in range(n):
                idx += 1
                if grid[i][j] == 1:
                    if i > 0 and grid[i-1][j] == 1:
                        uf.union(idx, idx-n) # idx - n is the previous idx in the same column
                    if j > 0 and grid[i][j-1] == 1:
                        uf.union(idx, idx-1) # idx - 1 is the previous idx in the same row
                    maxarea = max(maxarea, uf.size[uf.find(idx)])
        return maxarea

