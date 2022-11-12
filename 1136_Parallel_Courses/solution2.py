import collections


class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        Kahn
        T:O(V+E) S:O(V+E)
        Runtime: 232 ms, faster than 94.51% of Python online submissions for Parallel Courses.
        Memory Usage: 15.4 MB, less than 100.00% of Python online submissions for Parallel Courses.
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        indegree = [0]*(N+1)
        graph = collections.defaultdict(list)
        for s, e in relations:
            indegree[e] += 1
            graph[s].append(e)

        queue = []
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        ans = 0
        while queue:
            l = len(queue)
            ans += 1
            for i in range(l):
                curr = queue.pop(0)
                N -= 1
                for child in graph[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
        return -1 if N != 0 else ans