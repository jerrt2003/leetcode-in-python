import collections
from typing import List, Dict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build indgree mapping for each nodes
        # also build a neighbor maps for quick ref
        indgree: List[int] = [0 for _ in range(numCourses)]
        neighbors: Dict[int, List[int]] = collections.defaultdict(list)
        for course, require in prerequisites:
            indgree[course] += 1
            neighbors[require].append(course)

        # check nodes with indgree == 0 and place into queue (init queue)
        q = []
        for idx, count in enumerate(indgree):
            if count == 0:
                q.append(idx)

        # BFS: when node visited, numCourses - 1
        # all its neighbor's indgree count reduce by 1
        while q:
            course = q.pop(0)
            numCourses -= 1
            for neighbor in neighbors[course]:
                indgree[neighbor] -= 1
                if indgree[neighbor] == 0:
                    q.append(neighbor)

        # check if numCourses == 0
        return numCourses == 0
