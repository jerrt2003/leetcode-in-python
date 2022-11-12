# -*- coding: utf-8 -*-
import copy
class Solution(object):
    def shortestDistance(self, grid):
        """
        Solution: BFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (1684ms, beat only 0.98%)
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or grid[0] is None: return -1
        m = len(grid)
        n = len(grid[0])
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        q = set()
        block = set()
        distance_map = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    block.add((i, j))
                    distance[i][j] = -1
                    if grid[i][j] == 1:
                        q.add((i, j))

        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        def BFS(node, distance_from_house):
            bfs_q = [node]
            visited = set(node)
            while bfs_q:
                i, j = bfs_q.pop(0)
                for dir_x, dir_y in directions:
                    x = i+dir_x
                    y = j+dir_y
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and distance[x][y] != -1:
                        distance_from_house[x][y] = distance_from_house[i][j] + 1
                        bfs_q.append((x, y))
                        visited.add((x, y))
            distance_map.append(distance_from_house)


        for i, j in q:
            distance_from_house = copy.deepcopy(distance)
            distance_from_house[i][j] = 0
            BFS((i, j), distance_from_house)

        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if (i, j) in block: continue
                total_dist = 0
                for maps in distance_map:
                    total_dist += maps[i][j]
                min_dist = min(min_dist, total_dist)


        return -1 if min_dist == float('inf') else min_dist

#grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#grid = [[1]]
#grid = [[0,2,1],[1,0,2],[0,1,0]]

grid = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]

print Solution().shortestDistance(grid)