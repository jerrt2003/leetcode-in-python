# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    """
    Time Complexity: O(V(V+E))
    Space Complexity: O(E)
    """
    def shortestCirclePath(self, edges):

        def bfs(v):
            _level = 0
            stack = dir_maps[v][:]
            while stack:
                _level += 1
                for i in range(len(stack)):
                    next_stop = stack.pop(0)
                    if next_stop == v: # loop found
                        return _level
                    else:
                        if next_stop not in dir_maps:
                            continue # no more neighbor to go
                        for neighbor in dir_maps[next_stop]:
                            stack.append(neighbor)
            return float('inf')

        dir_maps = hash2.defaultdict(list)
        for s, e in edges:
            dir_maps[s].append(e)
        level = float('inf')
        for v in dir_maps:
            level = min(bfs(v), level)

        return None if level == float('inf') else level


edges = [(1, 2),(2, 3),(2, 5),(2, 6),(3, 4),(4, 1),(5, 1), (6, 1)]
#edges = [(1,2),(2,3),(1,3)]

print Solution().shortestCirclePath(edges)