import collections
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        node_neighbors = collections.defaultdict(list)
        indegree = [0 for _ in range(n + 1)]

        for s, e in relations:
            node_neighbors[s].append(e)
            indegree[e] += 1

        q = []
        courseTaken = 0
        ans = 0
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            l = len(q)
            ans += 1
            for _ in range(l):
                course = q.pop(0)
                courseTaken += 1
                for next_course in node_neighbors[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        q.append(next_course)

        return -1 if courseTaken != n else ans
