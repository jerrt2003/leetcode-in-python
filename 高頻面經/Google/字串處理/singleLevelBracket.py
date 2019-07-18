# -*- coding: utf-8 -*-
class Solution(object):
    def getAllCombination(self, s):

        def findCombo(idx):
            cache = ''
            while idx < len(s):
                if s[idx] == '}':
                    return idx, cache.split(',')
                else:
                    cache += s[idx]
                idx += 1

        res, i = [''], 0
        while i < len(s):
            if s[i] == '{':
                i, combo = findCombo(i+1)
                res = [a+b for a in res for b in combo]
            else:
                res = [a+s[i] for a in res]
            i += 1

        return res




#assert Solution().getAllCombination('{a,b}c{d,e}f') == ['acdf','acef','bcdf','bcef']
assert Solution().getAllCombination('a{b{c,d}e{f}}')