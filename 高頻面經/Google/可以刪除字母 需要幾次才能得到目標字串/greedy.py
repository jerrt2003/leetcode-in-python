# -*- coding: utf-8 -*-
class Solution(object):
    def countReconstruct(self, source, target):
        pt_target = 0
        count = 0
        while pt_target < len(target):
            pt_source = 0
            while pt_source < len(source) and pt_target < len(target):
                if source[pt_source] == target[pt_target]:
                    pt_source += 1
                    pt_target += 1
                else:
                    pt_source += 1
            count += 1
        return count

src = "abcadb"
aim = "aaaa"

print Solution().countReconstruct(src, aim)