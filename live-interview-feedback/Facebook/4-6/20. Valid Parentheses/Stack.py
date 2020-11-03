# -*- coding: utf-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (20ms, beating 100%)
        :type s: str
        :rtype: bool
        """
        stack = []
        for _s in s:
            if _s in ('(', '{', '['):
                stack.append(_s)
            else:
                if not stack:
                    return False
                elif _s == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif _s == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif _s == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
        if not stack:
            return True
        else:
            return False