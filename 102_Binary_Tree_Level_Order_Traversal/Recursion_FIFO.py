# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def levelOrder(self, root):
        """
        Solution: Recursion + FIFO
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF !!
        Thinking Process:
        - USE FIFO Queue
        - 每一個level有自己的queue(這樣才有辦法分層)
        - 只有當stack_for_next_level不等於0時我們才需要在往下做(不然會有無線迴圈)
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        stack = [root]
        self.find(stack)
        return self.res


    def find(self, stack):
        level_result = []
        stack_for_next_level = []
        while len(stack) != 0:
            node = stack.pop(0)
            if node is None: continue
            if node.left is not None:
                stack_for_next_level.append(node.left)
            if node.right is not None:
                stack_for_next_level.append(node.right)
            level_result.append(node.val)
        self.res.append(level_result)
        if len(stack_for_next_level) != 0:
            self.find(stack_for_next_level)

