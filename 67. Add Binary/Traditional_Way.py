# -*- coding: utf-8 -*-
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        adding_len = min(len(a), len(b))
        res = ''
        while adding_len
