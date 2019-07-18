# -*- coding: utf-8 -*-
class Solution(object):
    def checkIfAlive(self, matrix, start_i, start_j):
        stack = [(start_i, start_j)]
        visited = set()
        m = len(matrix)
        n = len(matrix[0])
        while stack:
            i, j = stack.pop(0)
            visited.add((i, j))
            for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    if matrix[x][y] == '0':
                        return False
                    elif matrix[x][y] == '2' and (x, y) not in visited:
                        stack.append((x, y))
        return True