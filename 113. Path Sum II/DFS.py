# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - very similar to Q.112
        - However we need to consider not only positive, also we need to check negative situation
            - for example: 3
            - possible answer:
                - 1 + 2
                - 3 + (-5) + 2 + 3
            - which means we need check all the way to the leaf node (can't cut the DFS short)
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None: return []
        self.res = []
        self.sum = sum
        self.findPath(root, 0, [])
        return self.res

    def findPath(self, node, sum, path):
        sum += node.val
        curr_path = path[:]
        curr_path.append(node.val)
        if sum == self.sum and node.left is None and node.right is None:
            self.res.append(curr_path)
            return
        if node.left is not None:
            self.findPath(node.left, sum, curr_path)
        if node.right is not None:
            self.findPath(node.right, sum, curr_path)

node_1 = TreeNode(-2)
node_2 = TreeNode(-3)
node_1.right = node_2

sol = Solution()
print sol.pathSum(node_1, -5)