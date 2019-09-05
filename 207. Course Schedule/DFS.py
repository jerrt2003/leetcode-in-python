# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        Template:
        L ← Empty list that will contain the sorted nodes
        while exists nodes without a permanent mark do
        select an unmarked node n
        visit(n)

        function visit(node n)
            if n has a permanent mark then return
            if n has a temporary mark then stop   (not a DAG)
            mark n with a temporary mark
            for each node m with an edge from n to m do
                visit(m)
            remove temporary mark from n
            mark n with a permanent mark
            add n to head of L


        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def dfs(i, maps, state):
            if state[i] == -1:
                return False
            else:
                state[i] = -1
                for neighbor in maps[i]:
                    if not dfs(neighbor, maps, state):
                        return False
                state[i] = 1
                return True

        maps = hash2.defaultdict(list)
        for k, v in prerequisites:
            maps[v].append(k)
        state = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if state[i] != 1:
                if not dfs(i, maps, state):
                    return False
        return True


