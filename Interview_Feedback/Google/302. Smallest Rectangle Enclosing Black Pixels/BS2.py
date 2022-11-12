# -*- coding: utf-8 -*-
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        n = len(image[0])
        rowHasPixel = [False] * m
        colHasPixel = [False] * n
        for i, row in enumerate(image):
            if '1' in row:
                rowHasPixel[i] = True
        for j, col in enumerate(zip(*image)):
            if '1' in col:
                colHasPixel[j] = True

        def bs(l, r, search=None):
            while l < r:
                mid = (l + r - 1) / 2
                if search == 'row':
                    if rowHasPixel:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if colHasPixel:
                        r = mid
                    else:
                        l = mid + 1
                return l

        def revBs(l, r, search=None):
            while l < r:
                mid = (l + r - 1) / 2
                if search == 'row':
                    if not rowHasPixel:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if not colHasPixel:
                        r = mid
                    else:
                        l = mid + 1
                return l

        # find upper
        l, r = 0, x + 1
        upper = bs(l, r, 'row')

        # find lower
        l, r = x, m
        lower = revBs(l, r, 'row')

        # find left
        l, r = 0, y + 1
        left = bs(l, r, 'col')

        # find lower
        l, r = y, n
        right = revBs(l, r, 'col')

        return (lower - upper) * (right - left)
