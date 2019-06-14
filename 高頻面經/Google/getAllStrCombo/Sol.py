# -*- coding: utf-8 -*-
class Solution(object):
    def getAllPossibleOutput(self, str):
        """
        Time: O(n)
        Space: O(n)
        :param str:
        :return:
        """
        def insideBracket(str, i):
            cache = ''
            while i < len(str):
                if str[i] == '}':
                    return cache, i
                else:
                    cache += str[i]
                i += 1

        i = 0
        res = ['']
        while i < len(str):
            if str[i] == '{':
                subStr, i = insideBracket(str, i+1)
                res = [a+b for a in res for b in subStr.split(',')]
            else:
                res = [a+str[i] for a in res]
            i += 1

        return res

assert Solution().getAllPossibleOutput('a{1,2,3}{b,c}') == ['a1b','a1c','a2b','a2c','a3b','a3c']