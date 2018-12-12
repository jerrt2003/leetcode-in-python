# -*- coding: utf-8 -*-
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        Solution: DP + DFS
        Time Complexity:
        Space Complexity:
        Inspired By:
        - https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
        - https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90812/Simple-commented-java-solution-with-thinking-progress-O(n)
        TP:
        - instead of finding if each cell can reach pacific or atlantic, we flip the thinking process and "let pac/atl try to flow into center of matrix"
        - Which means for if any cell enter our dfs, its previous node (which it coming from) must able to reach pac/atl
        - We scan the matrix top/bottom then left/right
        - Then for both pac/atl is True we add to res
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None or len(matrix) == 0: return []
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.dir = [(1,0),(-1,0),(0,1),(0,-1)]
        pac = [[False for _ in range(self.col)] for _ in range(self.row)]
        atl = [[False for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row): # scan from left col (pac) and right col (atl)
            self.dfs(i, 0, pac, matrix)
            self.dfs(i, self.col-1, atl, matrix)
        for j in range(self.col): # scan from top row (pac) and bottom row (atl)
            self.dfs(0, j, pac, matrix)
            self.dfs(self.row-1, j, atl, matrix)
        res = []
        for i in range(self.row):
            for j in range(self.col):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, i, j, visted, matrix):
        visted[i][j] = True
        for dir in self.dir:
            x, y = i + dir[0], j + dir[1]
            # !!! if visited, we don't need to check again (visited[x][y] = True)
            if x < 0 or x >= self.row or y < 0 or y >= self.col or visted[x][y] or matrix[i][j] > matrix[x][y]:
                continue
            self.dfs(x, y, visted, matrix)



sea = [[1,2,2,3,5],
       [3,2,3,4,4],
       [2,4,5,3,1],
       [6,7,1,4,5],
       [5,1,1,2,4]]
#sea = [[1,1],[1,1]]

sol = Solution()
print sol.pacificAtlantic(sea)