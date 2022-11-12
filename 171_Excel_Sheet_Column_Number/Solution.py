# -*- coding: utf-8 -*-
import math
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            digit = len(s)-i
            res = res + math.pow(26, digit-1)*(ord(s[i])-64)
        return int(res)


s = 'ZY'
sol = Solution()
print sol.titleToNumber(s)