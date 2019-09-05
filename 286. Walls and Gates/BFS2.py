# -*- coding: utf-8 -*-
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        Sol: BFS
        Perf: Runtime: 308 ms, faster than 42.69% / Memory Usage: 19.5 MB, less than 11.11%
        T: O(mn)
        S: O(mn)
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return None
        stack = []
        visit = set()
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    stack.append((i, j))
                    visit.add((i, j))
        while stack:
            x, y = stack.pop(0)
            for nextX, nextY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nextX < m and 0 <= nextY < n and rooms[nextX][nextY] >= 0 and (nextX, nextY) not in visit:
                    rooms[nextX][nextY] = min(rooms[nextX][nextY], rooms[x][y] + 1)
                    stack.append((nextX, nextY))
                    visit.add((nextX, nextY))

