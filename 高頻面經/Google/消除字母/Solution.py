# -*- coding: utf-8 -*-
class Solution(object):
    def stringDedup(self, words):
        stack = []
        for w in words:
            if not stack:
                stack.append(w)
            elif w.upper() == stack[-1].upper():
                stack.pop()
            else:
                stack.append(w)
        return ''.join(stack)

assert Solution().stringDedup('abBCcd') == 'ad'
assert Solution().stringDedup('abBCcAd') == 'd'