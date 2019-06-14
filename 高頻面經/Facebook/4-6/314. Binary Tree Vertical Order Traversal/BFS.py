# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        Sol: BFS + Hashmap (use to store col: elements)
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 20 ms, faster than 97.03% / Memory Usage: 11.8 MB, less than 68.42%
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        maps = collections.defaultdict(list)
        queue = collections.deque([(root,0)])
        min_col, max_col = 0, 0
        while queue:
            node, col = queue.popleft()
            maps[col].append(node.val)
            if node.left:
                min_col = min(min_col, col-1)
                queue.append((node.left, col-1))
            if node.right:
                max_col = max(max_col, col+1)
                queue.append((node.right, col+1))
        res = []
        for i in range(min_col, max_col+1):
            res.append(maps[i])
        return res
