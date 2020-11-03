# -*- coding: utf-8 -*-
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        curr = 0
        sign = 1
        for elem in s:
            if elem.isdigit():
                curr = 10 * curr + int(elem)
            elif elem == '+':
                res += sign * curr
                curr = 0
                sign = 1
            elif elem == '-':
                res += sign * curr
                curr = 0
                sign = -1
            elif elem == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif elem == ')':
                res += sign * curr
                res *= stack.pop()
                res += stack.pop()
                curr = 0
        if curr != 0:
            res += curr * sign
        return res

assert Solution().calculate("1-(5)")
