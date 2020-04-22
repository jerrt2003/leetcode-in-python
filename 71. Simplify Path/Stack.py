# -*- coding: utf-8 -*-
class Solution(object):
    def simplifyPath(self, path):
        """
        Solution: Stack + Split
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/simplify-path/discuss/25691/9-lines-of-Python-code
        :type path: str
        :rtype: str
        """
        path = [p for p in path.split('/') if p != '.' and p != '']
        stack = []
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)

path = "/../"
print Solution().simplifyPath(path)