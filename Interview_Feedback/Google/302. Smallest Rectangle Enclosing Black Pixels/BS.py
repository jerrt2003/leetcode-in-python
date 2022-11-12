# -*- coding: utf-8 -*-
class Solution(object):
    def minArea(self, image, x, y):
        """
        T: O(m+n+log(n))
        S: O(m+n)
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        n = len(image[0])
        havePixel_row = [False] * m
        havePixel_col = [False] * n

        for i, row in enumerate(image):
            if '1' in row:
                havePixel_row[i] = True

        for i, col in enumerate(zip(*image)):
            if '1' in col:
                havePixel_col[i] = True

        # get upper
        l, r = 0, x+1
        while l < r:
            mid = (l+r-1)/2
            if havePixel_row[mid]:
                r = mid
            else:
                l = mid+1
        upper = l

        l, r = x, m
        while l < r:
            mid = (l+r-1)/2
            if not havePixel_row[mid]:
                r = mid
            else:
                l = mid+1
        lower = l-1

        l, r = 0, y+1
        while l < r:
            mid = (l+r-1)/2
            if havePixel_col[mid]:
                r = mid
            else:
                l = mid+1
        left = l

        l, r = y, n
        while l < r:
            mid = (l+r-1)/2
            if not havePixel_col[mid]:
                r = mid
            else:
                l = mid+1
        right = l-1

        return (right-left+1) * (lower-upper+1)