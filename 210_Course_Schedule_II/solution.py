import collections

from typing import List, Dict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        # build indgree maps and neighbors maps
        indgree: List[int] = [0 for _ in range(numCourses)]
        neighbors: Dict[int, List[int]] = collections.defaultdict(list)
        for course, require in prerequisites:
            indgree[course] += 1
            neighbors[require].append(course)

        # check node with indgree == 0 and push into queue
        q = []
        for idx, count in enumerate(indgree):
            if count == 0:
                q.append(idx)

        # BFS, when a node is visited, push into ret
        # only push a node into queue when its indgree == 0
        while q:
            node = q.pop(0)
            ret.append(node)
            for neighbor in neighbors[node]:
                indgree[neighbor] -= 1
                if indgree[neighbor] == 0:
                    q.append(neighbor)

        # return ans else empty list if numCourses != 0
        return ret if len(ret) == numCourses else []
