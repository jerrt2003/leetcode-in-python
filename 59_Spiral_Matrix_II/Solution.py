# -*- coding: utf-8 -*-
class Solution(object):
    def generateMatrix(self, n):
        """
        Solution: Linear
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (32ms, beat 99.21%)
        TP:
        - Same approach as spiral matrix #54. Spiral Matrix
        :type n: int
        :rtype: List[List[int]]
        """
        num = 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        i_top, i_bottom, j_left, j_right = 0, n-1, 0, n-1
        while i_top < i_bottom or j_left < j_right:
            for j in range(j_left, j_right):
                num += 1
                res[i_top][j] = num
            for i in range(i_top, i_bottom):
                num += 1
                res[i][j_right] = num
            for j in range(j_right, j_left, -1):
                num += 1
                res[i_bottom][j] = num
            for i in range(i_bottom, i_top, -1):
                num += 1
                res[i][j_left] = num
            i_top += 1
            i_bottom -= 1
            j_left += 1
            j_right -= 1
        if i_top == i_bottom:
            for j in range(j_left, j_right+1):
                num += 1
                res[i_top][j] = num
        elif j_left == j_right:
            for i in range(i_top, i_bottom+1):
                num += 1
                res[i][j_left] = num
        return res

print Solution().generateMatrix(4)