# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        T:O(n) S:O(n)
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return 0, None
            l, l_lca = dfs(node.left)
            r, r_lca = dfs(node.right)
            if l > r:
                return l+1, l_lca
            elif r > l:
                return r+1, r_lca
            return l+1, node

        return dfs(root)[1]