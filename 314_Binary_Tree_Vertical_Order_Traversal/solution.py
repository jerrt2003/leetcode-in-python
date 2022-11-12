# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        Facebook
        Tree
        BFS
        T:O(V) S:O(V)
        Runtime: 20 ms, faster than 85.46% of Python online submissions for Binary Tree Vertical Order Traversal.
        Memory Usage: 12.8 MB, less than 48.57% of Python online submissions for Binary Tree Vertical Order Traversal.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        column = collections.defaultdict(list)
        queue = collections.deque([])
        ans = []
        if not root:
            return ans

        queue.append((root, 0))
        while queue:
            node, col_idx = queue.popleft()
            column[col_idx].append(node.val)
            if node.left:
                queue.append((node.left, col_idx - 1))
            if node.right:
                queue.append((node.right, col_idx + 1))
        idx = sorted(column.keys())
        for i in idx:
            ans.append(column[i])
        return ans