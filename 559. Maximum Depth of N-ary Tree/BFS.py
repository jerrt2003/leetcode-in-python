# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        Solution: BFS (172 ms, beat 9.87%)
        Time Complexity: O(n) (n: number of nodes)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        q = [root]
        level = 0
        while q:
            for i in range(len(q)):
                tmp = q.pop(0)
                if tmp.children:
                    for child in tmp.children:
                        q.append(child)
            level += 1
        return level