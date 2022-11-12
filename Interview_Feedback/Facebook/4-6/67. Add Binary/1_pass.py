# -*- coding: utf-8 -*-
class Solution(object):
    def addBinary(self, a, b):
        """
        Perf: Runtime: 24 ms, faster than 79.61% / Memory Usage: 11.8 MB, less than 29.80%
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1
        res = []
        carry = 0
        while m > -1 and n > -1:
            total = carry + int(a[m]) + int(b[n])
            carry = total / 2
            rem = total % 2
            res.append(str(rem))
            m -= 1
            n -= 1
        while m > -1:
            total = carry + int(a[m])
            carry = total / 2
            rem = total % 2
            res.append(str(rem))
            m -= 1
        while n > -1:
            total = carry + int(b[n])
            carry = total / 2
            rem = total % 2
            res.append(str(rem))
            n -= 1
        if carry != 0:
            res.append('1')
        res = ''.join(res[::-1])
        return res if res else '0'
