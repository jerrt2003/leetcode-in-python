# -*- coding: utf-8 -*-
class Soltuion(object):
    def screenCanFit(self, screen_width, screen_height, string, fontSize):
        def canFit(fontSize, string):
            h = getHeight(fontSize)
            w = 0
            for c in string:
                w += getWidth(c, fontSize)
            '''
            chrPerRow = screen_width / w
            chrPerCol = screen_height / h
            return chrPerCol*chrPerRow >= len(string)
            '''
            return screen_width*screen_height >= w*h

        l, r = 0, len(fontSize)
        while l < r:
            m = (l+r-1)/2
            if canFit(m):
                r = m
            else:
                l = m+1
        return fontSize[l]