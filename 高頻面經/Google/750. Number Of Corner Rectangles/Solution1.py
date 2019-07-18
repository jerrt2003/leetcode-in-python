# -*- coding: utf-8 -*-
class Solution(object):
    def countCornerRectangles(self, grid):
        """
        Time: O(m**2*n)
        Space: O(1)
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)-1):
            for j in range(i+1, len(grid)):
                count = 0
                for v1, v2 in zip(grid[i],grid[j]):
                    if v1 == v2 == 1:
                        res += count
                        count += 1
        return res