# -*- coding: utf-8 -*-
class Solution(object):
    def getAllCombo(self, str):
        def insideBracket(str, i):
            res = ['']
            cache = ''
            while i < len(str):
                if str[i] == '}':
                    res = [a+b for a in res for b in cache.split(',')]
                    return res, i+1
                elif str[i] == '{':
                    if cache is not None:
                        res = [a+cache for a in res]
                        cache = ''
                    sub_str, i = insideBracket(str, i+1)
                    res = [a+b for a in res for b in sub_str]
                else:
                    cache += str[i]
                    i += 1

        i = 0
        res = ['']
        while i < len(str):
            if str[i] == '{':
                sub_str, i = insideBracket(str, i+1)
                res = [a+b for a in res for b in sub_str]
            else:
                res = [a+str[i] for a in res]
                i += 1
        return res


#assert Solution().getAllCombo('a{1,2,3}{b,c}') == ['a1b','a1c','a2b','a2c','a3b','a3c']
#assert Solution().getAllCombo('a{b{1,2}c}{4,5}') == ['ab1c4','ab1c5','ab2c4','ab2c5']
#assert Solution().getAllCombo('a{b{1{c,d}2{e,f}3}g}') == ['ab1c2e3g','ab1d2f3g','ab1c2e3g','ab1d2f3g']