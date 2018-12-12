# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By:
        Thinking Process:
        - At any given node the max path will be node.val + max value from left child + max value from right child
        - 試著從最下面的節點 apply this algorithm
        Algorithm:
        - def findMaxPath(node):
            if node is None: return 0 -> 沒有node沒有value
            leftsum = max(0, findMaxPath(node.left)) -> 找左邊最大數值(最小為0因為我們不要negative number)
            rightsum = max(0, findMaxPath(node.right)) -> 找右邊最大數值(最小為0因為我們不要negative number)
            maxPath = max(maxPath, leftsum + rightsum + node.val) -> 根據該node的最大值判斷是否需要更新最大數值)
            return max(left, right) + node.val -> 回傳時我們只能回傳either左邊的樹或是右邊的數因為Path只能選一邊
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = -float('inf')
        self.findMaxPath(root)
        return self.maxPath

    def findMaxPath(self, node):
        if node is None: return 0
        leftsum = max(0, self.findMaxPath(node.left))
        rightsum = max(0, self.findMaxPath(node.right))
        self.maxPath = max(self.maxPath, leftsum+rightsum+node.val)
        return max(leftsum,rightsum) + node.val



