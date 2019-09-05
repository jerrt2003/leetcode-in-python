# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

import hash2
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res, stack = [], hash2.deque([])
        if root is None:
            return res
        else:
            stack.appendleft(root)
        while stack:
            node = stack.popleft()
            res.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    stack.appendleft(child)
        return res