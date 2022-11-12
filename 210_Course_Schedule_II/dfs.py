# -*- coding: utf-8 -*-
import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        Solution: DFS
        Perf: Runtime: 80 ms, faster than 82.48% / Memory Usage: 14.9 MB, less than 27.78%
        T: O(V+E)
        S: O(V+E)
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        visit = [0] * numCourses

        # build graph
        for end, start in prerequisites:
            graph[end].append(start)

        order = []

        def dfs(i):
            if visit[i] == 1:
                return True
            elif visit[i] == -1:
                return False
            else:
                visit[i] = -1
                for c in graph[i]:
                    if not dfs(c):
                        return False
                visit[i] = 1
                order.append(i)
                return True

        for i in range(numCourses):
            if not dfs(i):
                return None

        return order

numCourses = 2
prerequisites = [[1,0]]
assert Solution().findOrder(numCourses, prerequisites) == [0, 1]