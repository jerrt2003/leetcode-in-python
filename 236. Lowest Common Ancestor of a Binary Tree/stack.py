# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 88 ms, faster than 41.52% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
        Memory Usage: 20.6 MB, less than 92.76% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root: None}
        queue = collections.deque([root])
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ans = set()
        while p:
            ans.add(p)
            p = parent[p]

        while q not in ans:
            q = parent[q]

        return q

