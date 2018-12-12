# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        Solution: BFS
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        Thinking Process:
        - Create a list to store each level nodes
        - Do BFS search based on each level nodes
        - return when that level length == 0
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        if root is not None:
            self.findEachLevel([root])
        return self.res


    def findEachLevel(self, level_nodes):
        if len(level_nodes) == 0: return
        next_level_nodes = []
        val = []
        for node in level_nodes:
            if node.left is not None:
                next_level_nodes.append(node.left)
            if node.right is not None:
                next_level_nodes.append(node.right)
            val.append(node.val)
        self.res.insert(0, val)
        self.findEachLevel(next_level_nodes)
