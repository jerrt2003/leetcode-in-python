# -*- coding: utf-8 -*-
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.res = None
        self.avg = -float('inf')
        self.getSum(root)

        return self.res


    def getSum(self, node):
        if node is None:
            return None, None
        curr_sum, dividen = node.val, 1
        sum_left, left_kids_counts = self.getSum(node.left)
        if sum_left:
            curr_sum += sum_left
            dividen += left_kids_counts
        sum_right, right_kids_count = self.getSum(node.right)
        if sum_right:
            curr_sum += sum_right
            dividen += right_kids_count
        cur_avg = float(curr_sum) / dividen
        if cur_avg > self.avg:
            self.res = node
            self.avg = cur_avg
        return curr_sum, dividen