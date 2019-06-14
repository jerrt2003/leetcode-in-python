# -*- coding: utf-8 -*-
class Solution(object):
    def findClosetNodeInBST(self, root, target):
        if root.val == target:
            return root.val
        elif root.left.val < target < root.val:
            if abs(target-root.left.val) > abs(target-root.val):
                return root.val
            else:
                return root.left.val
        elif root.val < target < root.right.val:
            if abs(target-root.right.val) > abs(target-root.val):
                return root.val
            else:
                return root.right.val
        elif target <= root.left.val:
            return self.findClosetNodeInBST(root.left, target)
        elif target >= root.right.val:
            return self.findClosetNodeInBST(root.right, target)
