# -*- coding: utf-8 -*-
class Solution(object):
    def deserialize(self, s):
        key = ''
        curr = ''
        res = dict()
        for c in s:
            if c not in ('"',':',',','{','}'):
                curr += c
            elif c == '"':
                if len(curr) != 0:
                    if len(key) > 0:
                        res[key] = curr
                        curr = ''
                        key = ''
                    else:
                        key = curr
                        curr =''
        return res

a = '{"abc":"123","cde":"456"}'
print Solution().deserialize(a)