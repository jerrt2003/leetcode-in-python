# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Solution: Kahn's Algorithm (topo sort)
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        incoming = collections.defaultdict(list)
        outgoing = collections.defaultdict(list)
        for k, v in prerequisites:
            incoming[k].append(v)
            outgoing[v].append(k)
        topo_sort = []
        tmp = [] # to store nodes with no incoming edges
        for i in range(numCourses):
            if i not in incoming:
                tmp.append(i)
        while tmp:
            x = tmp.pop(0)
            topo_sort.append(x)
            for neighbor in outgoing[x]:
                incoming[neighbor].remove(x)
                if not incoming[neighbor]:
                    tmp.append(neighbor)
                    del incoming[neighbor]
        if len(incoming) > 0:
            return False
        else:
            return True