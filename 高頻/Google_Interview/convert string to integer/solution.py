# -*- coding: utf-8 -*-
import math
class Solution(object):
    def convert(self, input):
        a, b = input.split('.')
        res = 0
        # dealing with value more than 1
        if a.startswith('-'):
            negative = -1
            a = a[1:]
        else:
            negative = 1
        p = 0
        for char in a[::-1]:
            res += int(char) * math.pow(10, p)
            p += 1
        # dealing with less 1
        p = 0
        _less_than_one = 0
        for char in b[::-1]:
            _less_than_one += int(char) * math.pow(10, p)
            p += 1
        _less_than_one = float(_less_than_one) / math.pow(10, p)

        return (res + _less_than_one) * negative


print Solution().convert('172.98774')