# -*- coding: utf-8 -*-
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return reversed(s)

s = "hello"
sol = Solution()
print sol.reverseString(s)