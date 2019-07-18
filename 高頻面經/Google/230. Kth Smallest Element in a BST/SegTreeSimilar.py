# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def buildTreeWithCount(node):
            if not node:
                return None
            curr = NodeWithCount(node.val)
            leftNode = buildTreeWithCount(node.left)
            rightNode = buildTreeWithCount(node.right)
            if leftNode:
                curr.count += leftNode.count
                curr.left = leftNode
            if rightNode:
                curr.count += rightNode.count
                curr.right = rightNode
            return curr

        rootWithCount = buildTreeWithCount(root)

        def query(node, k):
            if k <= 0 or k > node.count:
                return -1
            if node.left:
                if node.left.count >= k:
                    return query(node.left, k)
                elif k-1 == node.left.count:
                    return node.val
                else:
                    return query(node.right, k - 1 - node.left.count)
            else:
                if k == 1:
                    return node.val
                else:
                    return query(node.right, k - 1)

        return query(rootWithCount, K)


class NodeWithCount(object):
    def __init__(self, val=None, count=None):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None