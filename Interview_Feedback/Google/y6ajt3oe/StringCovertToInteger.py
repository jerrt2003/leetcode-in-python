# -*- coding: utf-8 -*-
import math
class Solution(object):
    def strIntCoverter(self, str):
        a, b = str.split('.')
        res = 0
        n = 0
        for num in a[::-1]:
            res += math.pow(10,n)*int(num)
            n+=1
        n = 1
        for num in b:
            res += math.pow(0.1,n)*int(num)
            n+=1
        return res

assert Solution().strIntCoverter('141.3932') == 141.3932

