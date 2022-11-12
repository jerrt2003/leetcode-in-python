# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        Facebook
        T:O(n) S:O(1)
        
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l + r)
            return 1 + max(l, r)

        dfs(root)
        return self.ans
