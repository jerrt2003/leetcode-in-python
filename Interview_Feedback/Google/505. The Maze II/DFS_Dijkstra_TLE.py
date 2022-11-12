# -*- coding: utf-8 -*-
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if maze is None or len(maze) == 0: return -1
        row = len(maze)
        col = len(maze[0])
        distance = [[float('inf') for _ in range(col)] for _ in range(row)]
        visited = [[False for _ in range(col)] for _ in range(row)]
        distance[start[0]][start[1]] = 0

        def findMin(distance, visited):
            s = [-1, -1]
            _distance = float('inf')
            for i in range(row):
                for j in range(col):
                    if not visited[i][j] and distance[i][j] < _distance:
                        s = [i, j]
                        _distance = distance[i][j]
            return s

        def dijkstra(maze, distance, visited):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while True or visited[destination[0]][destination[1]]:
                s = findMin(distance, visited)
                if s == [-1, -1]:
                    break
                visited[s[0]][s[1]] = True
                for direction in directions:
                    count = 0
                    next_i = s[0] + direction[0]
                    next_j = s[1] + direction[1]
                    while next_i >=0 and next_i < row and next_j >=0 and next_j < col and maze[next_i][next_j] != 1:
                        count += 1
                        next_i += direction[0]
                        next_j += direction[1]
                    current_i = next_i - direction[0]
                    current_j = next_j - direction[1]
                    if distance[current_i][current_j] > distance[s[0]][s[1]] + count:
                        distance[current_i][current_j] = distance[s[0]][s[1]] + count

        dijkstra(maze, distance, visited)

        if distance[destination[0]][destination[1]] != float('inf'):
            return distance[destination[0]][destination[1]]
        else:
            return -1

maze = [[0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1],
        [0,0,0,0,1,0,0]]

#maze = []


start = [0, 0]
end = [8, 6]

sol = Solution()
print sol.shortestDistance(maze, start, end)