# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        Facebook
        Sol: Level BFS
        Perf: Runtime: 16 ms, faster than 97.15% / Memory Usage: 12 MB, less than 25.00%
        T: O(n)
        S: O(n)
        Key: For a complete binary tree, there should not be any node after we met an empty one.
        :type root: TreeNode
        :rtype: bool
        """
        i, stack = 0, [root]
        while stack[i]:
            stack.append(stack[i].left)
            stack.append(stack[i].right)
            i += 1
        return not any(stack[i:])
