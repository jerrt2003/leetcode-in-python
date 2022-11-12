# -*- coding: utf-8 -*-
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        Stack
        T:O(n) S:O(n)
        Runtime: 24 ms, faster than 19.28% of Python online submissions for Score of Parentheses.
        Memory Usage: 12.8 MB, less than 38.55% of Python online submissions for Score of Parentheses.
        :type S: str
        :rtype: int
        """
        stack = [0]
        for s in S:
            if s == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(val*2, 1)
        return stack[0]

print Solution().scoreOfParentheses('(())()')