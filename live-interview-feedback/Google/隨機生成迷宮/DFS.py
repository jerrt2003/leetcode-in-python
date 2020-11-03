# -*- coding: utf-8 -*-
import random
class Solution(object):
    def generateMaze(self, m, n, i, j, x, y):
        maze = [[1 for _ in range(n)] for _ in range(m)]
        dir = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i, j):
            maze[i][j] = 0
            _dir = dir[:]
            random.shuffle(_dir)
            for i_diff, j_diff in _dir:
                next_x, next_y = i+2*i_diff, j+2*j_diff
                wall_x, wall_y = i+i_diff, j+j_diff
                if 0 <= next_x < m and 0 <= next_y < n and maze[next_x][next_y] == 1 and maze[wall_x][wall_y] != 'X':
                    maze[wall_x][wall_y] = 0
                    dfs(next_x, next_y)

        dfs(i, j)
        for row in maze:
            print row

Solution().generateMaze(9,9,0,0,4,5)