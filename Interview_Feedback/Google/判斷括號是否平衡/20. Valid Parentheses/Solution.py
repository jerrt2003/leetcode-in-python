# -*- coding: utf-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 24 ms, faster than 52.55% / Memory Usage: 11.7 MB, less than 85.06%
        :type s: str
        :rtype: bool
        """
        stack = []
        for _s in s:
            if _s in ['{','[','(']:
                stack.append(_s)
            elif _s == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif _s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif _s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0