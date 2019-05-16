# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        self.maps = dict()
        self.dfs(head)
        return self.maps[head]

    def dfs(self, node):
        if node is None:
            return None
        if node in self.maps:
            return self.maps[node]
        dup = Node(node.val, None, None)
        self.maps[node] = dup
        dup.next = self.dfs(node.next)
        dup.random = self.dfs(node.random)
        return dup