# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def findBestApartments(self, blocks, requirements):
        m = len(blocks)
        blockToRequire = [{req: float('inf') for req in requirements} for _ in range(m)]
        for i in range(m):
            for req in requirements:
                blocks[i] = set(blocks[i])
                if req in blocks[i]:
                    blockToRequire[i][req] = 0
                elif i-1 >= 0:
                    blockToRequire[i][req] = blockToRequire[i-1][req] + 1
        for i in range(m-1, -1, -1):
            for req in requirements:
                if req in blocks[i]: continue
                elif i+1 < m:
                    blockToRequire[i][req] = min(blockToRequire[i][req], blockToRequire[i+1][req]+1)
        min_dist = float('inf')
        res = []
        for i in range(m):
            block_max_dist = max(blockToRequire[i].values())
            if block_max_dist < min_dist:
                min_dist = block_max_dist
                res = [i]
            elif block_max_dist == min_dist:
                res.append(i)
        return res

street = [["Store", "School", "Museum"],["Hospital", "Restaurant"],["School", "Restaurant"],[],["Museum"]]
requirements = ["Store", "Museum", "Restaurant"]
assert Solution().findBestApartments(street, requirements) == [0, 1]