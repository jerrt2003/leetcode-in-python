# -*- coding: utf-8 -*-
import copy
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        distance = [[0 for _ in range(n)] for _ in range(m)]
        bld = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    distance[i][j] = float('inf')
                    if grid[i][j] == 1:
                        bld.append((i, j))
        all_bld_to_house = []
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for bld_x, bld_y in bld:
            bld_to_house = copy.deepcopy(distance)
            bld_to_house[bld_x][bld_y] = 0
            bfs_q = [(bld_x, bld_y)]
            visited = set(bfs_q)
            while bfs_q:
                i, j = bfs_q.pop(0)
                for I, J in directs:
                    x = i+I
                    y = j+J
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                        bld_to_house[x][y] = bld_to_house[i][j] + 1
                        bfs_q.append((x, y))
                        visited.add((x, y))
            all_bld_to_house.append(bld_to_house)

        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                total = 0
                for dist in all_bld_to_house:
                    total += dist[i][j]
                min_dist = min(min_dist, total)

        return min_dist

#grid = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]
grid = [[0,2,1],[1,0,2],[0,1,0]]
print Solution().shortestDistance(grid)