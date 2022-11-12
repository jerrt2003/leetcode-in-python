# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        T:O(n) S:O(n)
        Runtime: 20 ms, faster than 71.83% of Python online submissions for Leaf-Similar Trees.
        Memory Usage: 12.8 MB, less than 53.08% of Python online submissions for Leaf-Similar Trees.
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, lst):
            if not root.left and not root.right:
                lst.append(root.val)
                return
            if root.left:
                dfs(root.left, lst)
            if root.right:
                dfs(root.right, lst)

        lst1, lst2 = [], []
        dfs(root1, lst1)
        dfs(root2, lst2)
        return lst1 == lst2