import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Facebook
        T:O(V+E) S:O(V)
        Runtime: 72 ms, faster than 98.81% of Python online submissions for Course Schedule.
        Memory Usage: 16.3 MB, less than 13.05% of Python online submissions for Course Schedule.
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = [0] * numCourses

        graph = collections.defaultdict(list)

        for s, e in prerequisites:
            graph[e].append(s)

        def dfs(i):
            if visit[i] == -1:
                return False
            elif visit[i] == 1:
                return True
            visit[i] = -1
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if visit[i] == 0:
                if not dfs(i):
                    return False

        return True