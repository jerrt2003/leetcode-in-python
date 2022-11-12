# -*- coding: utf-8 -*-
class Solution(object):
    def reverseStringInsideParenthesis(self, s):
        stack = []
        m = len(s)
        i = 0
        while i < m:
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                prev = stack.pop()
                s = s[:prev] + s[prev:i][::-1] + s[i:]
            i += 1
        #return ''.join([w for w in s if w not in ('(',')')])
        def checkIsChar(w):
            return w.isalpha()
        return filter(checkIsChar,s)


s = 'ab(cd)'
assert Solution().reverseStringInsideParenthesis(s) == 'abdc'
s = 'ab(cd(ef))'
assert Solution().reverseStringInsideParenthesis(s) == 'abefdc'