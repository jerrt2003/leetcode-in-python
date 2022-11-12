import collections


class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        Toposort Kahns Algorithem
        T:O(V+E) S:O(V+E)
        Runtime: 872 ms, faster than 5.49% of Python online submissions for Parallel Courses.
    Memory Usage: 16.8 MB, less than 100.00% of Python online submissions for Parallel Courses.
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        in_graph = collections.defaultdict(set)
        out_graph = collections.defaultdict(set)
        for start, end in relations:
            in_graph[end].add(start)
            out_graph[start].add(end)
        visit = set()
        level = 0
        queue = []
        for i in range(1, N+1):
            if i not in in_graph.keys():
                queue.append(i)
        while queue:
            level += 1
            for i in range(len(queue)):
                curr = queue.pop(0)
                visit.add(curr)
                for node in out_graph[curr]:
                    in_graph[node].remove(curr)
                    if len(in_graph[node]) == 0:
                        queue.append(node)

        return -1 if len(visit) != N else level

print Solution().minimumSemesters(3,[[1,3],[2,3]])
print Solution().minimumSemesters(3,[[1,2],[2,3],[3,1]])