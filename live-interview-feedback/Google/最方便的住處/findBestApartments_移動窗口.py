# -*- coding: utf-8 -*-
import collections


class Solution(object):
    def findBestApartments(self, blocks, req):
        """
        To return a list of idx which has smallest range to all req
        :param blocks: list[list]
        :param req: list
        :return: list
        """
        window = float('inf')
        bkt = collections.Counter()
        pt1 = pt2 = 0
        req = set(req)
        res = []
        while pt2 < len(blocks):
            for i in blocks[pt2]:
                if i in req:
                    bkt[i] += 1
            while len(bkt) == len(req):
                if pt2 - pt1 <= window:
                    mid = (pt2 + pt1)/2
                    rem = (pt2 + pt1)%2
                    if pt2 - pt1 < window:
                        if rem == 0:
                            res = [mid]
                        else:
                            res = [mid, mid+1]
                        window = pt2 - pt1
                    else:
                        if rem == 0:
                            res.append(mid)
                        else:
                            res.extend([mid, mid+1])
                for i in blocks[pt1]:
                    if i in req:
                        bkt[i] -= 1
                        if bkt[i] == 0:
                            del bkt[i]
                pt1 += 1
            pt2 += 1

        return res


blocks = [['A'],['B','C'],['D','E','F'],['G'],['B','F'],['A','C','E'],['D'],['F','G'],['B','E']]
req = ['A','E','G']

assert Solution().findBestApartments(blocks, req)