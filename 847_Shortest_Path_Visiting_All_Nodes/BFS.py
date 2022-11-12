# -*- coding: utf-8 -*-
class Solution(object):
    def shortestPathLength(self, graph):
        """
        Solution: BFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/135809/Fast-BFS-Solution-(46ms)-Clear-Detailed-Explanation-Included
        TP:
        - Few trick:
            - Use bits to record visit status (faster than using set)
            - Since we are using BFS, the first we met all bits mark as 1, it is the shortest path
        :type graph: List[List[int]]
        :rtype: int
        """
        q = []
        visited = set()
        N = len(graph)
        for i in range(N):
            tmp = 1 << i
            q.append([tmp, i, 0])
            visited.add((tmp, i))
        while q:
            curr_map, curr_node, cost = q.pop(0)
            if curr_map == (1 << N) -1:
                return cost
            else:
                for neighbor in graph[curr_node]:
                    tmp = curr_map | (1 << neighbor)
                    if (tmp, neighbor) not in visited:
                        q.append([tmp, neighbor, cost+1])
                        visited.add((tmp, neighbor))
        return -1

graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print Solution().shortestPathLength(graph)