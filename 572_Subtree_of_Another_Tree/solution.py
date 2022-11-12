# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 252 ms, faster than 74.71% of Python online submissions for Subtree of Another Tree.
        Memory Usage: 13.9 MB, less than 53.23% of Python online submissions for Subtree of Another Tree.
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return compare(node1.left, node2.left) and compare(node1.right, node2.right)
            return False

        def dfs(node):
            if not node:
                return False
            if node.val == t.val:
                if compare(node, t):
                    return True
            return dfs(node.left) or dfs(node.right)

        return dfs(s)