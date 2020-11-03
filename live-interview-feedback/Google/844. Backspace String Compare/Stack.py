# -*- coding: utf-8 -*-
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (36ms, beat 15.08%)
        :type S: str
        :type T: str
        :rtype: bool
        """
        def evaluate(target):
            stack = []
            for char in target:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
                else:
                    stack = []
            return stack

        return evaluate(S) == evaluate(T)

