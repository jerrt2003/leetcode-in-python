# -*- coding: utf-8 -*-
class Solution(object):
    def shortestPath(self, src, dst, maze):
        """
        Solution: BFS
        :param src:
        :param dst:
        :param maze:
        :return:
        """
        stack = [src]
        res = 0
        m = len(maze)
        n = len(maze[0])
        while stack:
            for _ in range(len(stack)):
                i, j = stack.pop()
                if (i, j) == dst:
                    return res+1
                maze[i][j] = 'X'
                for i_diff, j_diff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x, y = i+i_diff, j+j_diff
                    if 0 <= x < m and 0 <= y < n and maze[x][y] != 0 and maze[x][y] != 'X':
                        stack.append((x, y))
            res += 1
        return 0

maze = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]

src = (0, 0)
dst = (3, 4)

print Solution().shortestPath(src, dst, maze)