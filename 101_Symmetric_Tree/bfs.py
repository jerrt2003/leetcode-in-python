# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root]
        while stack:
            v = []
            l = len(stack)
            for _ in range(l):
                curr = stack.pop(0)
                if curr.left:
                    v.append(curr.left.val)
                    stack.append(curr.left)
                else:
                    v.append('X')
                if curr.right:
                    v.append(curr.right.val)
                    stack.append(curr.right)
                else:
                    v.append('X')
            if v != v[::-1]:
                return False

        return True