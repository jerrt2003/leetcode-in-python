# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def matchingChar(self, str1, str2):
        def findPattern(str):
            _firstHit = collections.defaultdict(int)
            pattern = []
            for i in range(len(str)):
                if str[i] not in _firstHit:
                    _firstHit[str[i]] = i
                pattern.append(_firstHit[str[i]])
            return pattern

        return findPattern(str1) == findPattern(str2)

assert Solution().matchingChar('ABCBB','XQZQQ') == True
assert Solution().matchingChar('ABCB','ABCA') == False
assert Solution().matchingChar('ABCB','CXYX') == True
assert Solution().matchingChar('ABCD','XYZF') == True


