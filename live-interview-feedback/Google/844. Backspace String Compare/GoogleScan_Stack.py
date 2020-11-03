# -*- coding: utf-8 -*-
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 24 ms, faster than 54.36% / Memory Usage: 11.9 MB, less than 5.06%
        :type S: str
        :type T: str
        :rtype: bool
        """

        def textEditor(S):
            stack = []
            for s in S:
                if not stack and s != '#':
                    stack.append(s)
                elif s != '#':
                    stack.append(s)
                elif stack:
                    stack.pop()
            return stack

        return textEditor(S) == textEditor(T)