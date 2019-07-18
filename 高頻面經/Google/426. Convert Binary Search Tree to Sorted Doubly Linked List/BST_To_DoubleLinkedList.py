# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        BST+Sorted: Inorder
        T:O(n)
        S:O(1)
        Perf: Runtime: 796 ms, faster than 87.87% / Memory Usage: 202 MB, less than 41.48%
        :type root: Node
        :rtype: Node
        """
        self.head, self.last = None, None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.head = node
            self.last = node
            dfs(node.right)

        if not root:
            return None

        dfs(root)
        self.head.left = self.last
        self.last.right = self.head
        return self.head


