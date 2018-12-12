# -*- coding: utf-8 -*-
class Solution(object):
    def toLowerCase(self, str):
        """
        Using ORD
        :type str: str
        :rtype: str
        """
        res = ''
        for char in str:
            if ord(char) in range(ord('A'),ord('Z')+1):
                res += chr(ord(char)+32)
            else:
                res += char
        return res

str = "Hello"
print Solution().toLowerCase(str)