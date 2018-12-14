# -*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        stack = []
        seen = set()
        for l in s[::-1]:
            if not l in seen:
                stack.append(l)
                seen.add(l)
            else:
                if ord(l) < ord(stack[-1]):
                    stack.remove(l)
                    stack.append(l)
        return ''.join(stack[::-1])

s = "cbc"
print Solution().removeDuplicateLetters(s)