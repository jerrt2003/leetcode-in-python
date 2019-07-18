# -*- coding: utf-8 -*-
import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        T: O(m*nlog(m*n))
        S: O(m*n)
        Perf: Runtime: 260 ms, faster than 97.12% / Memory Usage: 12.1 MB, less than 73.33%
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        visited = set()
        q = []
        heapq.heappush(q, (0, (start[0], start[1])))
        while q and (destination[0], destination[1]) not in visited:
            x, y = heapq.heappop(q)[1]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for x_diff, y_diff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_x = x + x_diff
                next_y = y + y_diff
                count = 0
                while 0 <= next_x < m and 0 <= next_y < n and maze[next_x][next_y] != 1:
                    next_x += x_diff
                    next_y += y_diff
                    count += 1
                next_x -= x_diff
                next_y -= y_diff
                if dist[next_x][next_y] > dist[x][y] + count:
                    dist[next_x][next_y] = dist[x][y] + count
                    heapq.heappush(q, (dist[x][y] + count, (next_x, next_y)))

        return dist[destination[0]][destination[1]] if dist[destination[0]][destination[1]] != float('inf') else -1


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
end = [3,2]
assert Solution().shortestDistance(maze, start, end) == -1