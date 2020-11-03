# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def usingDFStoSolveShortestLoop(self, edges):
        dist_v = set()
        maps = collections.defaultdict(list)
        for s, e in edges:
            maps[s].append(e)
            dist_v.add(s)
            dist_v.add(e)

        def dfs(v, level, status):
            if status[v-1] == -1: # loop found
                self.res = min(level, self.res)
                return True
            elif v in maps:
                status[v-1] = -1
                for next in maps[v]:
                    if dfs(next, level+1, status):
                        return True
                status[v-1] = 1
            return False

        self.res = float('inf')
        for v in maps:
            status = [0 for _ in range(len(dist_v))]
            dfs(v, 0, status)

        return None if self.res == float('inf') else self.res-1

edges = [(1, 2),(2, 3),(2, 5),(2, 6),(3, 4),(4, 1),(5, 1), (6, 1)]
#edges = [(1,2),(2,3),(1,3)]

print Solution().usingDFStoSolveShortestLoop(edges)


