# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        BFS + DFS
        Runtime: 44 ms, faster than 46.75% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
        Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Lowest Common Ancestor of Deepest Leaves.
        :type root: TreeNode
        :rtype: TreeNode
        """
        def findLCA(root, l, r):
            # T:O(n) S:O(1)
            if root is None or root.val in [l.val, r.val]:
                return root
            left = findLCA(root.left, l, r)
            right = findLCA(root.right, l, r)
            if left and right:
                return root
            if left:
                return left
            return right

        # T:O(n) S:O(n)
        prev_level = []
        curr_level = [root]
        while curr_level:
            prev_level = curr_level[:]
            for i in range(len(curr_level)):
                node = curr_level.pop(0)
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)

        if len(prev_level) == 1:
            return prev_level[0]

        return findLCA(root, prev_level[0], prev_level[-1])