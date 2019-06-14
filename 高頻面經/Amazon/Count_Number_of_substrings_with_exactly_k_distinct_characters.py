# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def countSubStringWithK(self, target, k):
        m = len(target)
        res = 0
        for i in range(m):
            for j in range(i, m):
                count = collections.Counter(target[i:j+1])
                if len(count) == k:
                    res += 1
        return res

target = 'abcbaa'
k = 3
print Solution().countSubStringWithK(target, k)