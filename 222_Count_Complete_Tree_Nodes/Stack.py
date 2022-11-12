# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def __init__(self):
        self.stack = []

    def countNodes(self, root):
        """
        Solution: Stack
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF !!
        Thinking Process:
        - Do a DFS, if this level is complete node, we add all nodes at this level into a list and append to a stack
        - Once we found a non-complete level, we return False
        - At this time we will know the last complete nodes(self.stack[-1])
        - We will also know the last level of complete nodes(len(self.stack)
        - We compute the number of complete nodes + non-complete level nodes number
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self.stack = [[root]]
        while self.is_next_level_complete(self.stack[-1]):
            continue
        # find the last level nodes
        count = 0
        for node in self.stack[-1]:
            if node.left is not None:
                count += 1
            else:
                break
            if node.right is not None:
                count += 1
            else:
                break
        for i in range(len(self.stack)):
            count += int(math.pow(2,i))
        return count


    def is_next_level_complete(self, stack):
        new_stack = []
        for node in stack:
            if node.left is None or node.right is None:
                return False
            new_stack.append(node.left)
            new_stack.append(node.right)
        self.stack.append(new_stack)
        return True