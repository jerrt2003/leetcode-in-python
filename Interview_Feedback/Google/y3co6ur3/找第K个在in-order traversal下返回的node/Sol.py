# -*- coding: utf-8 -*-
class Solution(object):
    def findKthElementInTree(self, node, k):
        if k == 1 and not node.left:
            return node
        if k <= node.left + 1:
            return self.findKthElementInTree(node.left, k)
        k -= node.left+1
        if k == 1:
            return node
        else:
            return self.findKthElementInTree(node.right, k-1)