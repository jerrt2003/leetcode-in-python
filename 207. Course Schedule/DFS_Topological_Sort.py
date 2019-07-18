# -*- coding: utf-8 -*-
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Solution: DFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By:
        - https://en.wikipedia.org/wiki/Topological_sorting
        - https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
        TP:
        - Need to understand the question: basically prerequisites present the relation between the class we plan to take
            - We need to verify if this plan ("Prerequites") is valid or not !!
        - Topological Sorting: to find if there is a loop in given graph
        - create a list to mark node status as we travel through each node
            - the node has 3 status:
                - 0: init state
                - 1: visited (means no loop starting from this node) !!!!!!
                - -1: is being visited in current DFS iteration, if we hit "-1" means we have a loop
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.course = [[] for _ in range(numCourses)]
        self.visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            self.course[y].append(x)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True
        self.visit[i] = -1
        for j in self.course[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True
