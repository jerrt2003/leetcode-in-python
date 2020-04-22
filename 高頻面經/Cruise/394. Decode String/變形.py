# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        def dfs(i):
            cache = ''
            while i < len(s):
                if s[i].isalpha():
                    cache += s[i]
                elif s[i] == '(':
                    res, i = dfs(i+1)
                    cache += res[::-1]
                elif s[i] == ')':
                    return cache, i
                i += 1
            return cache, i

        res, _ = dfs(0)
        return res

s = 'ab(cd)'
assert Solution().decodeString(s) == 'abdc'
s = 'ab(cd(ef))'
assert Solution().decodeString(s) == 'abefdc'