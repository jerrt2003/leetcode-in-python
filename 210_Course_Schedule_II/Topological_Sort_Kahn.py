# -*- coding: utf-8 -*-
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        Solution: Topo Sort (Kahn's Algorithm)
        Time Complexity: O(M+N) (M: number of nodes, N: number of edges)
        Space Complexity: O(M+N)
        Inspired By: MySELF + https://en.wikipedia.org/wiki/Topological_sorting
        TP:
        - Although Accepted, only beat 0.96% people... (1104 ms)
        - This is better version (36 ms, beat 98%):
            - Create another list called: required_by_other_course for reference
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses = [[] for _ in range(numCourses)]
        required_by_other_course = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            courses[x].append(y)
            required_by_other_course[y].append(x)
        res = []
        next_in_line = []
        for i in range(numCourses):
            if not courses[i]:
                next_in_line.append(i)
        while next_in_line:
            current_check = next_in_line.pop(0)
            res.append(current_check)
            for i in required_by_other_course[current_check]:
                courses[i].remove(current_check)
                if not courses[i]:
                    next_in_line.append(i)
        for value in courses:
            if value:
                return []
        return res

#n = 4
#p = [[1,0],[2,0],[3,1],[3,2]]

#n = 2
#p = [[1,0]]

n = 3
p = []

print Solution().findOrder(n, p)