# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def findBestApartments(self, blks, reqs):
        m = len(blks)
        pt1, pt2, l, r, min_dist = 0, 0, None, None, float('inf')
        bucket = collections.defaultdict(int)
        while pt2 < m:
            for req in reqs:
                if req in set(blks[pt2]):
                    bucket[req] += 1
            while len(bucket.keys()) > len(reqs)-1:
                dist = pt2-pt1+1
                if dist < min_dist:
                    min_dist = dist
                    l, r = pt1, pt2
                for facility in blks[pt1]:
                    if facility in bucket:
                        bucket[facility] -= 1
                        if bucket[facility] == 0:
                            del bucket[facility]
                pt1 += 1
            pt2 += 1
        print l, r

#blks = [['a'],['b','c'],['f'],['a','b','e'],['d']]
#reqs = ['a','c','d']

blks = [["Store", "School", "Museum"],["Hospital", "Restaurant"],["School", "Restaurant"],[],["Museum"]]
#reqs = ["Store", "Museum", "Restaurant"]
reqs = ["Hospital", "Restaurant"]

Solution().findBestApartments(blks, reqs)