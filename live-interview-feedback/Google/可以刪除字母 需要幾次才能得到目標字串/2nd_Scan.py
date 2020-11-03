# -*- coding: utf-8 -*-
class Solution(object):
    def findRepetitionCount(self, source, target):
        count, i, j = 0, 0, 0
        while i < len(target):
            if target[i] == source[j]:
                i += 1
            j += 1
            if j == len(source):
                count += 1
                j = 0
        return count + 1

assert Solution().findRepetitionCount('aabbcc','aabbaaacbbb') == 5