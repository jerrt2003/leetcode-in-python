# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        Perf: Runtime: 60 ms, faster than 99.88% / Memory Usage: 21.4 MB, less than 58.19%
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        curr = self.stack.pop()
        if curr.right:
            node = curr.right
            while node:
                self.stack.append(node)
                node = node.left
        return curr.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return not len(self.stack) == 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()