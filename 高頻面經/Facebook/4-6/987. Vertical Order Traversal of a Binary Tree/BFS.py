# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def verticalTraversal(self, root):
        """
        Perf: Runtime: 16 ms, faster than 97.54% / Memory Usage: 12.1 MB, less than 46.51%
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        _res = collections.defaultdict(list)

        def _traversal(node):
            stack = [(node, 0)]
            while stack:
                _tmp = collections.defaultdict(list)
                for i in range(len(stack)):
                    _node, column = stack.pop(0)
                    _tmp[column].append(_node.val)
                    if _node.left:
                        stack.append((_node.left, column - 1))
                    if _node.right:
                        stack.append((_node.right, column + 1))
                for k, v in _tmp.iteritems():
                    _res[k] += sorted(v)

        _traversal(root)
        min_k = min(_res.keys())
        max_k = max(_res.keys())
        res = []
        for k in range(min_k, max_k + 1):
            res.append(_res[k])
        return res
