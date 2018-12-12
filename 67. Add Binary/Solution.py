# -*- coding: utf-8 -*-
class Solution(object):
    def addBinary(self, a, b):
        """
        TP: convert string to int using base 2 (binary): int(<string>, base) then covert to string
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = bin(int(a, 2)+int(b, 2))
        print sum[2:]

a = "1010"
b = "1011"

sol = Solution()
sol.addBinary(a, b)
