# -*- coding: utf-8 -*-
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.node = dict()
        for prereq in prerequisites:
            if prereq[1] in self.node:
                self.node[prereq[1]].add(prereq[0])
            else:
                tmp = set()
                tmp.add(prereq[0])
                self.node[prereq[1]] = tmp
        for start_pt in self.node.keys():
            if self.check_course([start_pt], self.node[start_pt], numCourses-1):
                return True
            else:
                return False

    def check_course(self, path, candidate_courses, num):
        for next_course in candidate_courses:
            if next_course in path:
                continue
            if num == 0:
                return True
            else:
                current_path = path[:]
                current_path.append(next_course)
                self.check_course(current_path, self.node[next_course], num-1)
        return False

num = 2
course = [[1,0]]

sol = Solution()
print sol.canFinish(num, course)