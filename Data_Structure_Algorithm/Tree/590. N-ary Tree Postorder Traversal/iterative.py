# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

import collections
class Solution(object):
    def postorder(self, root):
        """
        Solution: iterative
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 696 ms, faster than 51.11% / Memory Usage: 107.6 MB, less than 43.62%
        :type root: Node
        :rtype: List[int]
        """
        if root is None: return []
        res, stack = [], collections.deque([root])
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for child in node.children:
                    stack.append(child)
        return res[::-1]