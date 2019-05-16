# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        Solution: recursive
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 848 ms, faster than 18.55% / Memory Usage: 107.7 MB, less than 16.01%
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node is None:
            return
        if node.children:
            for child in node.children:
                self.helper(child)
        self.res.append(node.val)