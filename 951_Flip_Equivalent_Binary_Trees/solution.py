# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        Tree
        T:O(n) S:O(1)
        Runtime: 16 ms, faster than 91.63% of Python online submissions for Flip Equivalent Binary Trees.
        Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Flip Equivalent Binary Trees.
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right))