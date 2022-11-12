# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        Solution: BFS
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        Thinking Process:
        - Do BFS
        - Store each level nodes into a list(ex. res)
        - Then return last node.val of each level
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if root is None: return []
        self.findLevelNodes([root])
        result = []
        for each_level_nodes in self.res:
            result.append(each_level_nodes[-1].val)
        return result

    def findLevelNodes(self, level_nodes):
        if len(level_nodes) == 0: return
        self.res.append(level_nodes)
        new_level_nodes = []
        for node in level_nodes:
            if node.left is not None:
                new_level_nodes.append(node.left)
            if node.right is not None:
                new_level_nodes.append(node.right)
        self.findLevelNodes(new_level_nodes)