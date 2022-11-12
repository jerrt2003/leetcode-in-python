# -*- coding: utf-8 -*-
class Solution(object):
    def shortestDistance(self, maze, start, end):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        row = len(maze)
        col = len(maze[0])
        DP = [[float('inf') for _ in range(col)] for _ in range(row)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def check_destination(destination):
            i = destination[0]
            j = destination[1]
            if i == 0 or i == len(maze) -1 or j == 0 or j == len(maze[0])-1:
                return True
            if maze[i-1][j] == 0 and maze[i+1][j] == 0 and maze[i][j-1] == 0 and maze[i][j+1] == 0:
                return False
            return True

        def dfs(i, j, i_dir, j_dir, current_dist, current_path):
            DP[i][j] = min(DP[i][j], current_dist)
            next_i = i + i_dir
            next_j = j + j_dir
            if next_i < 0 or next_i >= row or next_j < 0 or next_j >= col or maze[next_i][next_j] == 1:
                if i == end[0] and j == end[1]:
                    return
                else:
                    if (i, j) in current_path:
                        current_path[(i, j)].append((i_dir, j_dir))
                    else:
                        current_path[(i, j)] = [(i_dir, j_dir)]
                    for x in range(3):
                        i_dir, j_dir = -j_dir, i_dir
                        next_i = i + i_dir
                        next_j = j + j_dir
                        if next_i > -1 and next_i < row and next_j > -1 and next_j < col and maze[next_i][next_j] != 1:
                            if (next_i, next_j) not in current_path or (i_dir, j_dir) not in current_path[(next_i, next_j)]:
                                dfs(next_i, next_j, i_dir, j_dir, current_dist + 1, current_path)
            else:
                if (i, j) in current_path:
                    current_path[(i, j)].append((i_dir, j_dir))
                else:
                    current_path[(i, j)] = [(i_dir, j_dir)]
                dfs(next_i, next_j, i_dir, j_dir, current_dist+1, current_path)

        if not check_destination(end):
            return -1
        else:
            for directions in dirs:
                dfs(start[0], start[1], directions[0], directions[1], 0, {})
            return DP[end[0]][end[1]]
'''
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
'''

maze = [[0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1],
        [0,0,0,0,1,0,0]]

'''
start = [0, 4]
end = [4, 4]
'''

start = [0, 0]
end = [8, 6]

sol = Solution()
print sol.shortestDistance(maze, start, end)
