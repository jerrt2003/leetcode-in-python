from typing import List, Tuple

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # similar to tree traversal, but its a 'multi origin BFS'
        # first we mark all '1' to '-1' to indicate 'unvisited'
        # push all '0' into a queue (i.e. all '0' are root nodes)
        q: List[Tuple[int]] = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = -1
                else:
                    q.append((i, j))

        # as BFS goes, we also record 'level' (i.e. distance) of the BFS
        dist = 0
        while q:
            level_len = len(q)
            dist += 1
            for _ in range(level_len):
                node_cords = q.pop(0)
                for x, y in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
                    i, j = node_cords[0], node_cords[1]
                    i += x
                    j += y
                    if 0 <= i < m and 0 <= j < n and mat[i][j] == -1:
                        mat[i][j] = dist
                        q.append((i, j))

        # return ans
        return mat