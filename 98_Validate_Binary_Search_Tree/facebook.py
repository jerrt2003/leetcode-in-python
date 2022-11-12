# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        Facebook
        T:O(V) S:O(1)
        Runtime: 36 ms, faster than 73.09% of Python online submissions for Validate Binary Search Tree.
        Memory Usage: 17.4 MB, less than 53.94% of Python online submissions for Validate Binary Search Tree.
        :type root: TreeNode
        :rtype: bool
        """

        def isValid(node, left, right):
            if not node:
                return True
            if left and node.val <= left.val:
                return False
            if right and node.val >= right.val:
                return False
            return isValid(node.left, left, node) and isValid(node.right, node, right)

        return isValid(root, None, None)