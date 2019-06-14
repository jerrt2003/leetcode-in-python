# -*- coding: utf-8 -*-
class Solution(object):
    def checkBalanced(self, str):
        count = 0
        for s in str:
            if s == '(':
                count += 1
            else:
                count -= 1
        return count == 0

assert Solution().checkBalanced('(()))') == False
assert Solution().checkBalanced('(())()(())') == True
