# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        Solution: recursive
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 688 ms, faster than 50.66% / Memory Usage: 107.5 MB, less than 84.36%
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node is None:
            return
        self.res.append(node.val)
        if node.children:
            for child in node.children:
                self.helper(child)
        return