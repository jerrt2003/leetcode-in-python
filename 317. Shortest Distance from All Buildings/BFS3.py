# -*- coding: utf-8 -*-
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # calculate bld count
        bldCount = 0
        houseList = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bldCount += 1
                elif grid[i][j] == 0:
                    houseList.append((i, j))

        self.res = float('inf')
        for i, j in houseList:
            self.bfs(i, j, bldCount, grid, m, n)

        return self.res


    def bfs(self, i, j, bldCount, grid, m, n):
        level = 0
        stack = [(i, j)]
        totalDist = 0
        bldVisit = 0
        visit = set()
        while stack and bldVisit != bldCount:
            for _ in range(len(stack)):
                x, y = stack.pop(0)
                if grid[x][y] == 1:
                    totalDist += level
                    bldVisit += 1
                    visit.add((x, y))
                else:
                    for nextX, nextY in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
                        if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] != 2 and (nextX, nextY) not in visit and (nextX, nextY) not in stack:
                            stack.append((nextX, nextY))
            level += 1
        if bldVisit == bldCount:
            self.res = min(self.res, totalDist)

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
assert Solution().shortestDistance(grid) == 7