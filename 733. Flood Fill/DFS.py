# -*- coding: utf-8 -*-
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image is None or len(image) == 0: return None
        def fill(image, i, j, oldColor, newColer):
            if oldColor == newColor: return
            image[i][j] = newColer
            if i > 0 and image[i-1][j] == oldColor:
                fill(image, i-1, j, oldColor, newColer)
            if j > 0 and image[i][j-1] == oldColor:
                fill(image, i, j-1, oldColor, newColer)
            if i < len(image)-1 and image[i+1][j] == oldColor:
                fill(image, i+1, j, oldColor, newColer)
            if j < len(image[0])-1 and image[i][j+1] == oldColor:
                fill(image, i, j+1, oldColor, newColer)

        fill(image, sr, sc, image[sr][sc], newColor)
        return image
'''
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
'''
image = [[0,0,0],[0,1,1]]



sol = Solution()
print sol.floodFill(image, 1, 1, 1)
