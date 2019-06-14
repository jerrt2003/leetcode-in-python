# -*- coding: utf-8 -*-
class Solution(object):
    def longestConsecutivePath(self, matrix):
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        DP = [[0 for _ in range(m)] for _ in range(n)]

        def helper(i, j):
            if DP[i][j] == 0:
                lenUp = helper(i - 1, j) if 0 <= i - 1 < m and matrix[i][j] == matrix[i - 1][j] + 1 else 0
                lenDown = helper(i + 1, j) if 0 <= i + 1 < m and matrix[i][j] == matrix[i + 1][j] + 1 else 0
                lenLeft = helper(i, j - 1) if 0 <= j - 1 < n and matrix[i][j] == matrix[i][j - 1] + 1 else 0
                lenRight = helper(i, j + 1) if 0 <= j + 1 < n and matrix[i][j] == matrix[i][j + 1] + 1 else 0
                DP[i][j] = 1 + max(lenUp, lenDown, lenLeft, lenRight)
            return DP[i][j]

        for i in range(m):
            for j in range(n):
                helper(i, j)

        return max(DP[i][j] for i in range(m) for j in range(n))


#assert Solution().longestConsecutivePath([[1,2,3],[4,5,6],[7,8,9]]) == 3
assert Solution().longestConsecutivePath([[1,2,3],[6,5,4],[7,8,9]]) == 9
