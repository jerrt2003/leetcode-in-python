# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        """
        Solution: DFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - scanning the s from left to right and:
            - result: res = ''
            - multiply: multiply = ''
            - if we hit a close ']' which means we have a closed loop, return res and current i
                - res will be used in upper level recursion
                - to return current i will help upper level recursion to jump to right position (no re-calculate)
            - if we hit an alpha, add to current res (res += s[i])
            - if we hit and digit, add to multiply (multiply += s[i])
            - if we hit an open '[' which means we are hitting a new open brackets, then we need to do following 2 things:
                - call next level recursion and it will return a result and its index
                - this level res will be: res = res + int(multiply)*(next-level-recursion-result)
                - reset multiply to empty (empty = '') since we already count this multiply
            - continue to move index till string ends (i += 1)
        :type s: str
        :rtype: str
        """
        '''
        def decode(s, i):
            res = ''
            multiply = ''
            while i < len(s):
                if s[i] == ']':
                    return res, i
                elif s[i].isalpha():
                    res += s[i]
                elif s[i].isdigit():
                    multiply += s[i]
                elif s[i] == '[':
                    tmp, i = decode(s, i+1)
                    res = res + int(multiply)*tmp
                    multiply = ''
                i += 1
            return res, i
        '''

        def decode(s, i):
            res = ''
            multiply = ''
            while i < len(s):
                if s[i] == ']':
                    return res, i
                elif s[i].isalpha():
                    res += s[i]
                elif s[i].isdigit():
                    multiply += s[i]
                elif s[i] == '[':
                    tmp, i = decode(s, i+1)
                    res = res + int(multiply)*tmp

        res, i = decode(s, 0)
        return res

s = '3a'
sol = Solution()
print sol.decodeString(s)