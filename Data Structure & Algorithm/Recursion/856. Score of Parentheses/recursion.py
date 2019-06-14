# -*- coding: utf-8 -*-
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def parse(S, i):
            res = 0
            while i < len(S):
                if S[i] == ')':
