# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def findFirstIdxOfAnagram(self, s1, s2):
        counter = hash2.Counter(s2)
        pt1, pt2 = 0, len(s2)-1
        bkt = hash2.Counter(s1[pt1:pt2 + 1])
        while counter != bkt and pt2 < len(s1):
            bkt[s1[pt1]] -= 1
            if bkt[s1[pt1]] == 0:
                del bkt[s1[pt1]]
            pt1 += 1
            pt2 += 1
            bkt[s1[pt2]] += 1
        return pt1 if bkt == counter else -float('inf')


assert Solution().findFirstIdxOfAnagram('AAAAA','AAA') == 0
assert Solution().findFirstIdxOfAnagram('ABCDCDB','CDB') == 1