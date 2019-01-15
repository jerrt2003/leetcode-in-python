# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def minPathSum(self, grid):
        """
        Solution: Dijkestra
        Time Complexity:
        Space Complexity: O(m*n)
        Inspired By: MySELF!!
        TP:
        - In this question we are not allowed to go up or left
        :type grid: List[List[int]]
        :rtype: int
        """
        pq = []
        heapq.heappush(pq, (grid[0][0], (0, 0)))
        visited = set()
        m = len(grid)
        n = len(grid[0])
        #directions = [(-1, 0),(0, -1), (1, 0), (0, 1)]
        directions = [(1, 0), (0, 1)]
        while pq:
            cost, cord = heapq.heappop(pq)
            i, j = cord
            if not (i, j) in visited:
                visited.add(cord)
                if (i, j) == (m-1, n-1):
                    return cost
                else:
                    for x_dir, y_dir in directions:
                        x = x_dir + cord[0]
                        y = y_dir + cord[1]
                        if 0 <= x < m and 0 <= y < n:
                            heapq.heappush(pq, (cost + grid[x][y], (x, y)))

grid = [[5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],
        [3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],
        [6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],
        [4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8]]

print Solution().minPathSum(grid)