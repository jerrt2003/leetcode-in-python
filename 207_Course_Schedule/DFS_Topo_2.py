# -*- coding: utf-8 -*-
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course = [[] for _ in range(numCourses)]
        visit = [0] * numCourses

        for x, y in prerequisites:
            course[x].append(y)

        def dfs(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            else:
                visit[i] = -1
                for j in course[i]:
                    if not dfs(j):
                        return False
                visit[i] = 1
                return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


assert Solution().canFinish(2, [[1,0]]) == True