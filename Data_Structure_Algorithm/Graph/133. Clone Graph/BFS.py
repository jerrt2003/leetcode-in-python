# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        Solution: BFS
        Perf: Runtime: 44 ms, faster than 100.00% / Memory Usage: 12.9 MB, less than 13.93%
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param node:
        :return:
        """
        if not node:
            return
        copyNode = Node(node.val, [])
        maps = dict()
        maps[node] = copyNode
        stack = [node]
        while stack:
            curr = stack.pop(0)
            for _neighbor in curr.neighbors:
                if _neighbor in maps:
                    maps[curr].neighbors.append(maps[_neighbor])
                else:
                    newNode = Node(_neighbor.val, [])
                    maps[_neighbor] = newNode
                    maps[curr].neighbors.append(newNode)
                    stack.append(_neighbor)
        return copyNode